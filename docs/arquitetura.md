# Arquitetura — BluaDiagnostics Sprint 1

## Fluxograma em Mermaid

```mermaid
flowchart TD
    A[Usuário / Beneficiário] --> B[Entrada Conversacional]
    B --> C[System Prompt Clínico]
    C --> D[Memória de Sessão]
    D --> E[Identificação de Intenção]
    E --> F{Tipo de Solicitação}

    F -->|Check-up digital| G[Coleta de sintomas e sinais vitais]
    F -->|Histórico| H[Tool: consultar_historico_paciente]
    F -->|Medicamentos| I[Tool: verificar_interacoes_medicamentosas]
    F -->|Agendamento| J[Tool: agendar_teleconsulta]

    G --> K[Consulta à Knowledge Base simulada]
    H --> L[Contexto enriquecido]
    I --> L
    J --> L
    K --> L

    L --> M[LLM via Ollama Cloud]
    M --> N[Guardrails Clínicos]
    N --> O{Há red flag?}

    O -->|Sim| P[Escalada para atendimento humano]
    O -->|Não| Q[Resposta segura ao beneficiário]

    P --> R[Saída final]
    Q --> R[Saída final]
```

## Descrição

A arquitetura proposta simula um agente conversacional de apoio ao check-up digital. O fluxo começa com a entrada do beneficiário, passa pelo system prompt clínico, mantém memória de sessão, utiliza tools simuladas, consulta uma knowledge base inicial e retorna uma resposta segura com guardrails.

## Componentes

- **System Prompt Clínico:** define papel, escopo, restrições, formato de saída e escalada humana.
- **Memória de sessão:** preserva contexto entre turnos.
- **Roteamento de intenção:** identifica se o usuário precisa de check-up, histórico, verificação medicamentosa ou agendamento.
- **Tools simuladas:** representam integrações externas.
- **Knowledge Base:** documentos simulados para futura implementação de RAG.
- **Guardrails:** impedem diagnóstico definitivo, prescrição e respostas fora do escopo.
- **Human-in-the-loop:** decisões clínicas e prescrições dependem de profissional humano.
