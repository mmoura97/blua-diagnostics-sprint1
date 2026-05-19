# Arquitetura — BluaDiagnostics Sprint 1

```mermaid
flowchart TD
    A[Usuário / Beneficiário Blua] --> B[Chatbot com System Prompt Clínico]
    B --> C[Memória de Sessão]
    C --> D[Roteamento de Intenção]
    D --> E[Consulta RAG - Base Clínica Simulada]
    D --> F[Function Calling / Tools]
    F --> F1[consultar_historico_paciente]
    F --> F2[verificar_interacoes_medicamentosas]
    F --> F3[agendar_teleconsulta]
    E --> G[LLM]
    F --> G
    G --> H[Guardrails Clínicos e LGPD]
    H --> I[Resposta Estruturada]
    I --> J[Escalada Humana quando necessário]
```

## Descrição

O BluaDiagnostics recebe a mensagem do beneficiário, aplica o system prompt clínico, mantém memória de sessão e decide se precisa consultar tools simuladas. A resposta final é validada por guardrails clínicos, com foco em não diagnosticar, não prescrever sem médico e escalar casos de risco.
