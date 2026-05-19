import os
from pathlib import Path
from dotenv import load_dotenv
from ollama import Client

from src.tools import (
    consultar_historico_paciente,
    verificar_interacoes_medicamentosas,
    agendar_teleconsulta,
)

load_dotenv()


def carregar_system_prompt() -> str:
    path = Path(__file__).resolve().parents[1] / "prompts" / "system_prompt.md"
    return path.read_text(encoding="utf-8")


class BluaDiagnosticsAgent:
    def __init__(self):
        self.model = os.getenv("MODEL_NAME", "gpt-oss:120b")
        self.client = Client(
            host=os.getenv("OLLAMA_HOST", "https://ollama.com"),
            headers={"Authorization": "Bearer " + os.getenv("OLLAMA_API_KEY", "")},
        )
        self.system_prompt = carregar_system_prompt()
        self.memory = []

    def _detectar_tool(self, mensagem: str) -> tuple[str | None, dict]:
        texto = mensagem.lower()

        if "histórico" in texto or "historico" in texto:
            return "consultar_historico_paciente", {"paciente_id": "P001"}

        if "ibuprofeno" in texto or "dipirona" in texto or "medicamento" in texto:
            meds = []
            if "ibuprofeno" in texto:
                meds.append("ibuprofeno")
            if "dipirona" in texto:
                meds.append("dipirona")
            if not meds:
                meds.append("medicamento informado")
            return "verificar_interacoes_medicamentosas", {
                "paciente_id": "P001",
                "medicamentos_novos": meds,
            }

        if "agendar" in texto or "teleconsulta" in texto:
            return "agendar_teleconsulta", {
                "paciente_id": "P001",
                "especialidade": "clínica médica",
                "prioridade": "media",
                "motivo": mensagem,
            }

        return None, {}

    def _executar_tool(self, name: str, args: dict) -> dict:
        if name == "consultar_historico_paciente":
            return consultar_historico_paciente(**args)
        if name == "verificar_interacoes_medicamentosas":
            return verificar_interacoes_medicamentosas(**args)
        if name == "agendar_teleconsulta":
            return agendar_teleconsulta(**args)
        return {"erro": "Tool desconhecida."}

    def chat(self, mensagem: str) -> dict:
        tool_name, tool_args = self._detectar_tool(mensagem)
        tool_result = None

        if tool_name:
            tool_result = self._executar_tool(tool_name, tool_args)

        contexto_tool = ""
        if tool_result:
            contexto_tool = f"\nResultado da ferramenta {tool_name}: {tool_result}\n"

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.memory[-6:])
        messages.append({"role": "user", "content": mensagem + contexto_tool})

        response = self.client.chat(
            model=self.model,
            messages=messages,
            options={"temperature": 0.2, "num_predict": 350},
            stream=False,
        )

        resposta = response["message"]["content"].strip()

        self.memory.append({"role": "user", "content": mensagem})
        self.memory.append({"role": "assistant", "content": resposta})

        return {
            "resposta": resposta,
            "tool_chamada": tool_name,
            "tool_args": tool_args,
            "tool_result": tool_result,
        }
