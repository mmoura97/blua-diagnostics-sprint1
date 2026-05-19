import json
from pathlib import Path
from datetime import datetime, timedelta


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "mock_patient.json"


def _load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def consultar_historico_paciente(paciente_id: str) -> dict:
    dados = _load_data()
    paciente = dados["pacientes"].get(paciente_id)

    if not paciente:
        return {"erro": "Paciente não encontrado."}

    return {
        "paciente_id": paciente_id,
        "idade": paciente["idade"],
        "condicoes": paciente["condicoes"],
        "alergias": paciente["alergias"],
        "medicamentos_em_uso": paciente["medicamentos_em_uso"],
        "ultimas_consultas": paciente["ultimas_consultas"],
    }


def verificar_interacoes_medicamentosas(medicamentos_novos: list[str], paciente_id: str) -> dict:
    historico = consultar_historico_paciente(paciente_id)

    if "erro" in historico:
        return historico

    alertas = []
    alergias = [a.lower() for a in historico["alergias"]]
    uso_atual = [m.lower() for m in historico["medicamentos_em_uso"]]

    for medicamento in medicamentos_novos:
        med_lower = medicamento.lower()

        if any(alergia in med_lower for alergia in alergias):
            alertas.append(
                f"Atenção: {medicamento} pode estar relacionado a alergia registrada no histórico."
            )

        if "ibuprofeno" in med_lower and any("losartana" in m for m in uso_atual):
            alertas.append(
                "Possível cautela: anti-inflamatórios como ibuprofeno podem exigir avaliação médica em pacientes usando losartana."
            )

    return {
        "paciente_id": paciente_id,
        "medicamentos_avaliados": medicamentos_novos,
        "alertas": alertas,
        "status": "sem_interacoes_relevantes" if not alertas else "avaliacao_medica_recomendada",
    }


def agendar_teleconsulta(paciente_id: str, especialidade: str, prioridade: str, motivo: str) -> dict:
    data_sugerida = datetime.now() + timedelta(days=1)

    return {
        "paciente_id": paciente_id,
        "especialidade": especialidade,
        "prioridade": prioridade,
        "motivo": motivo,
        "status": "teleconsulta_simulada_agendada",
        "data_sugerida": data_sugerida.strftime("%Y-%m-%d %H:%M"),
    }
