# BluaDiagnostics — Sprint 1

PoC acadêmica para o Challenge Care Plus / Blua, focada em check-up digital conversacional e suporte seguro à prescrição remota com IA.

## Integrantes

| Nome | RM |
|---|---|
| Matheus Moura da Silva | RM566782 |
| Kaue Souza Rodrigues | RM557716 |
| Murylo Silva Amaral | RM568241 |
| Pedro Henrique Camacho de Alencar | RM568071 |
| Igor Mota Marran | RM567823 |

## Persona escolhida

**Beneficiário final em autoavaliação digital.**

A persona foi escolhida porque representa o primeiro contato do usuário com o BluaDiagnostics. O agente deve coletar sintomas, sinais vitais e contexto clínico inicial, sem substituir o médico.

## Problema

Transformar o Blua em uma plataforma de cuidado remoto proativo, permitindo check-up digital conversacional e suporte seguro a fluxos pós-teleconsulta.

## Stack técnica

- Python 3.10+
- Ollama Cloud API
- Modelo principal: `gpt-oss:120b`
- python-dotenv
- notebook Google Colab
- JSON Schema para tools
- arquitetura preparada para RAG e LangGraph em sprints futuras

## Comparação de modelos candidatos

| Critério | gpt-oss:120b via Ollama Cloud | Llama 3.2 3B via Ollama |
|---|---|---|
| Qualidade clínica esperada | Alta | Média |
| Latência | Média/alta | Baixa |
| Custo | Gratuito no contexto usado | Gratuito/local |
| Privacidade | Cloud | Pode ser local |
| Function calling | Simulado via orquestração Python | Simulado via orquestração Python |
| Justificativa | Melhor qualidade para respostas clínicas estruturadas | Alternativa leve para testes rápidos |

## Riscos clínicos e mitigações

| Risco | Mitigação |
|---|---|
| Alucinação médica | System prompt proíbe diagnóstico definitivo |
| Prescrição indevida | Humano-no-loop obrigatório |
| Red flags ignoradas | Protocolo de escalada humana |
| LGPD | Minimização de dados e uso de mocks |
| Viés | Eval set com cenários variados |

## Estrutura

```text
blua-diagnostics-sprint1/
├── README.md
├── requirements.txt
├── .env.example
├── docs/
│   └── arquitetura.md
├── prompts/
│   └── system_prompt.md
├── tools/
│   └── tools_spec.json
├── evals/
│   └── sprint1_eval_set.json
├── notebooks/
│   └── sprint1_poc.ipynb
├── knowledge_base/
│   └── *.md
├── data/
│   └── mock_patient.json
└── src/
    ├── agent.py
    └── tools.py
```

## Como executar localmente

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python
```

Configure a chave no `.env`:

```env
OLLAMA_API_KEY=sua_chave_aqui
OLLAMA_HOST=https://ollama.com
MODEL_NAME=gpt-oss:120b
```

## Notebook Colab

O notebook principal está em:

```text
notebooks/sprint1_poc.ipynb
```

Ele demonstra:

- system prompt aplicado;
- memória de conversa com múltiplos turnos;
- function calling simulado;
- tools clínicas mockadas;
- resposta estruturada com guardrails.

## Entrega

A entrega final da Sprint 1 deve ser um `.txt` contendo nomes, RMs e o link público do GitHub.
