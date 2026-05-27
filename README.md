# BluaDiagnostics — Sprint 1 | Care Plus

Repositório da Sprint 1 do Challenge **BluaDiagnostics**, proposta de IA conversacional para transformar o Blua em uma plataforma de cuidado remoto proativo.

A Sprint 1 tem foco em **exploração, arquitetura e prova de conceito**. O objetivo é demonstrar a viabilidade técnica de um agente conversacional com:

- system prompt clínico;
- memória de sessão;
- function calling simulado;
- base inicial para RAG;
- eval set com casos críticos;
- guardrails clínicos e LGPD;
- notebook executável no Google Colab.

---

## Integrantes

| Nome | RM |
|---|---|
| Matheus Moura da Silva | RM566782 |
| Kaue Souza Rodrigues | RM557716 |
| Murylo Silva Amaral | RM568241 |
| Pedro Henrique Camacho de Alencar | RM568071 |
| Igor Mota Marran | RM567823 |

---

## 1. Contexto do problema

A Care Plus já oferece recursos digitais como telemedicina, chatbot de atendimento, TytoCare e o app Blua. Entretanto, o Blua ainda é majoritariamente reativo, sendo usado para agendamento, autorização e consulta.

O BluaDiagnostics propõe uma evolução para uma jornada mais proativa, com dois pilares:

1. **Digital Check-up:** autoavaliação conversacional guiada por IA, com coleta de sintomas, sinais vitais e identificação de sinais de alerta clínico.
2. **Prescrição Remota Inteligente:** apoio pós-teleconsulta, sugerindo informações estruturadas para o médico, validando histórico e possíveis interações medicamentosas, sem substituir o profissional.

Nesta Sprint 1, o foco está na PoC do fluxo conversacional e nas decisões de arquitetura.

---

## 2. Persona escolhida

### Persona principal: beneficiário final em autoavaliação

**Nome fictício:** Renato Almeida  
**Idade:** 42 anos  
**Perfil:** beneficiário de plano premium, trabalha em rotina corporativa intensa, utiliza aplicativos de saúde e prefere resolver demandas simples pelo celular antes de falar com atendimento humano.  
**Contexto de uso:** Renato acessa o Blua para realizar um check-up digital rápido ao perceber sintomas leves, como dor de cabeça, tontura ou alteração de pressão.  
**Objetivo:** entender se seus sintomas indicam necessidade de teleconsulta, atendimento emergencial ou apenas monitoramento seguro.  
**Frustrações:** demora para decidir qual canal procurar, medo de subestimar sintomas, dúvidas sobre medicações e receio de receber orientação genérica.  
**Riscos principais:** interpretar resposta da IA como diagnóstico definitivo, omitir sintomas importantes ou tentar obter prescrição sem avaliação médica.

### Justificativa

A persona de beneficiário final foi escolhida porque representa o primeiro ponto de contato do cuidado proativo. O agente atua antes da teleconsulta, coletando informações, organizando sintomas, identificando red flags e encaminhando para humano quando necessário.

---

## 3. Stack técnica selecionada

| Componente | Escolha |
|---|---|
| Linguagem | Python 3.10+ |
| Ambiente da PoC | Google Colab / Jupyter Notebook |
| LLM principal | `gpt-oss:120b` via Ollama Cloud |
| SDK | `ollama` Python SDK |
| Prompting | System prompt clínico + memória de sessão |
| Tools | Function calling simulado via funções Python |
| RAG | Knowledge base simulada em arquivos `.txt` |
| Avaliação | Eval set JSON com 12 casos |
| Repositório | GitHub público |

---

## 4. Comparação entre modelos candidatos

| Critério | gpt-oss:120b via Ollama Cloud | llama3.2:3b via Ollama |
|---|---|---|
| Qualidade clínica esperada | Maior capacidade de seguir instruções complexas e lidar com contexto clínico | Adequado para testes simples, porém menos robusto em cenários clínicos |
| Latência média esperada | Maior, por ser modelo grande | Menor, por ser modelo leve |
| Custo por 1M tokens | Sem API paga direta no contexto do projeto; uso via Ollama Cloud conforme disponibilidade da conta | Sem API paga direta; mais leve e econômico para testes locais |
| Contexto máximo | Mais adequado para prompts longos e guardrails | Mais limitado para prompts extensos |
| Privacidade/on-premise | Pode depender da Ollama Cloud; não é totalmente on-premise | Pode ser executado localmente, favorecendo privacidade |
| Function calling | Simulado pela aplicação via Python | Simulado pela aplicação via Python |
| Adequação para Sprint 1 | Melhor escolha para demonstrar raciocínio, segurança e contexto | Alternativa para testes rápidos e baixo consumo |

### Modelo escolhido

O modelo escolhido para a PoC foi o **gpt-oss:120b via Ollama Cloud**, por apresentar maior capacidade de seguir instruções clínicas, respeitar guardrails e lidar com contexto mais longo. O `llama3.2:3b` foi considerado como alternativa leve para testes locais e menor latência.

---

## 5. Riscos clínicos, éticos e LGPD

| Risco | Impacto | Mitigação aplicada |
|---|---|---|
| Alucinação médica | Resposta incorreta pode induzir conduta inadequada | System prompt proíbe diagnóstico definitivo e prescrição |
| Diagnóstico indevido | Usuário pode interpretar orientação como diagnóstico | Respostas devem informar que a IA não substitui médico |
| Prescrição sem médico | Risco de automedicação | Agente não prescreve e encaminha para validação médica |
| Falha em red flags | Atraso em atendimento urgente | Eval set inclui sintomas críticos e system prompt força escalada |
| Viés clínico | Respostas diferentes por perfil do usuário | Linguagem padronizada, objetiva e baseada nos sintomas relatados |
| LGPD e dados sensíveis | Vazamento ou coleta excessiva de dados de saúde | Uso de dados mockados, minimização de dados e ausência de dados reais |
| Jailbreak | Usuário tenta forçar diagnóstico ou prescrição | Casos de jailbreak no eval set e restrições explícitas no prompt |
| Fora de escopo | Agente responde temas não relacionados à saúde | Casos out_of_scope no eval set e redirecionamento para o escopo correto |
| Responsabilidade clínica | IA pode ser vista como decisora final | Human-in-the-loop obrigatório para prescrição e decisão clínica |

---

## 6. Arquitetura proposta

O fluxograma está disponível em:

```text
docs/arquitetura.md
docs/arquitetura.svg
```

Fluxo resumido:

```text
Usuário
 ↓
Entrada Conversacional
 ↓
System Prompt Clínico + Memória
 ↓
Roteamento de Intenção
 ↓
RAG simulado + Tools
 ↓
LLM via Ollama Cloud
 ↓
Guardrails Clínicos
 ↓
Resposta Segura / Escalada Humana
```

---

## 7. Estrutura do projeto

```text
blua-diagnostics-sprint1/
├── README.md
├── requirements.txt
├── .env.example
├── docs/
│   ├── arquitetura.md
│   └── arquitetura.svg
├── evals/
│   └── sprint1_eval_set.json
├── knowledge_base/
│   ├── bula_losartana_resumida.txt
│   ├── cartilha_checkup_digital.txt
│   ├── politica_telemedicina_careplus.txt
│   ├── protocolo_interacoes_medicamentosas.txt
│   └── protocolo_red_flags.txt
├── notebooks/
│   └── sprint1_poc.ipynb
├── prompts/
│   └── system_prompt.md
├── src/
│   └── tools.py
└── tools/
    └── tools_spec.json
```

---

## 8. Notebook da PoC

Arquivo principal:

```text
notebooks/sprint1_poc.ipynb
```

A PoC demonstra:

- chamada ao LLM via Ollama Cloud;
- system prompt aplicado;
- memória conversacional com múltiplos turnos;
- consulta simulada a histórico do paciente;
- verificação simulada de interações medicamentosas;
- agendamento simulado de teleconsulta;
- resposta final segura com guardrails.

---

## 9. Function calling

As especificações das tools estão em:

```text
tools/tools_spec.json
```

Tools obrigatórias:

- `consultar_historico_paciente`
- `verificar_interacoes_medicamentosas`
- `agendar_teleconsulta`

As funções mockadas estão implementadas em:

```text
src/tools.py
```

---

## 10. Eval set

Arquivo:

```text
evals/sprint1_eval_set.json
```

O eval set contém 12 casos cobrindo:

- `happy_path`
- `red_flag`
- `jailbreak`
- `out_of_scope`

Cada caso possui:

- `id`
- `categoria`
- `entrada_usuario`
- `contexto_esperado`
- `resposta_ideal`
- `criterios_avaliacao`

---

## 11. Como executar no Google Colab

1. Abra o notebook:

```text
notebooks/sprint1_poc.ipynb
```

2. No Colab, acesse o menu lateral **Secrets**.

3. Crie o secret:

```text
OLLAMA_API_KEY
```

4. Execute todas as células.

---

## 12. Como executar localmente no VSCode

1. Criar ambiente virtual:

```bash
python -m venv venv
```

2. Ativar ambiente no Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Criar arquivo `.env`:

```env
OLLAMA_API_KEY=sua_chave_ollama
```

5. Abrir o notebook no VSCode e executar com a extensão Jupyter.

---

## 13. Segurança

Nenhuma chave de API deve ser enviada ao GitHub. Utilize `.env` localmente ou Secrets no Google Colab.

O arquivo `.gitignore` impede o envio de:

- `.env`
- `venv/`
- `__pycache__/`
- checkpoints de notebook

---

## 14. Observação médica

Este projeto é uma PoC acadêmica. O agente não substitui atendimento médico, não diagnostica e não prescreve medicamentos. Em situações de risco, o fluxo orienta escalada para atendimento humano.
