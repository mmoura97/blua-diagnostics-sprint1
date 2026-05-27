## Versão corrigida conforme feedback

A versão revisada da Sprint 1 está na branch:

https://github.com/mmoura97/blua-diagnostics-sprint1/tree/sprint1-final

# BluaDiagnostics — Sprint 1

Projeto acadêmico desenvolvido para o Challenge BluaDiagnostics utilizando Prompt Engineering, memória conversacional, function calling simulado e integração com Ollama Cloud.

---

# Objetivo

O objetivo desta Sprint 1 foi desenvolver uma prova de conceito (PoC) de IA conversacional aplicada ao contexto clínico da Care Plus.

O sistema simula um agente inteligente capaz de:

* auxiliar beneficiários em check-ups digitais;
* apoiar fluxos pós-teleconsulta;
* utilizar memória conversacional;
* aplicar guardrails clínicos;
* utilizar Prompt Engineering;
* demonstrar function calling;
* preparar a arquitetura para RAG na Sprint 2.

---

# Técnicas Utilizadas

Durante o desenvolvimento foram utilizadas técnicas de Prompt Engineering avaliadas previamente no CP02:

* Zero-Shot Prompting
* Few-Shot Prompting
* Chain-of-Thought Prompting
* Role Prompting

---

# Arquitetura da Solução

```text
Usuário
   ↓
System Prompt Clínico
   ↓
Memória Conversacional
   ↓
Function Calling Simulado
   ↓
Ollama Cloud
   ↓
Resposta Segura
```

---

# Estrutura do Projeto

```text
blua-diagnostics-sprint1/
├── docs/
├── evals/
├── knowledge_base/
├── notebooks/
├── prompts/
├── src/
├── tools/
├── README.md
├── requirements.txt
├── .env.example
└── entrega_sprint1.txt
```

---

# Funcionalidades Implementadas

## Memória Conversacional

O agente mantém histórico de mensagens durante múltiplos turnos de conversa.

---

## Function Calling Simulado

Foram implementadas tools mockadas para demonstrar integração com sistemas externos:

* consultar_historico_paciente
* verificar_interacoes_medicamentosas
* agendar_teleconsulta

---

## Guardrails Clínicos

O system prompt possui restrições para:

* evitar diagnósticos definitivos;
* evitar prescrição de medicamentos;
* escalar situações críticas para atendimento humano;
* respeitar princípios de LGPD.

---

## Knowledge Base

A pasta `knowledge_base/` contém documentos simulados que serão utilizados futuramente para RAG na Sprint 2.

---

# Tecnologias Utilizadas

* Python 3.12
* Google Colab
* Jupyter Notebook
* Ollama Cloud
* VSCode
* GitHub

---

# Como Executar o Projeto

## 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/blua-diagnostics-sprint1.git
```

---

## 2. Acessar a Pasta do Projeto

```bash
cd blua-diagnostics-sprint1
```

---

## 3. Criar Ambiente Virtual

### Windows

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# Configuração da Chave Ollama

## Ambiente Local (VSCode)

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_API_KEY=sua_chave_ollama
```

---

## Google Colab

No menu lateral do Colab:

```text
🔑 Secrets
```

Criar:

```text
OLLAMA_API_KEY
```

Inserir a chave do Ollama Cloud.

---

# Execução do Notebook

Abrir:

```text
notebooks/sprint1_poc.ipynb
```

---

## No VSCode

Instalar as extensões:

* Python
* Jupyter

Depois:

```text
Run All
```

---

## No Google Colab

Abrir o notebook diretamente pelo GitHub:

```text
File → Open Notebook → GitHub
```

Selecionar:

```text
notebooks/sprint1_poc.ipynb
```

Executar:

```text
Run All
```

---

# Estrutura de Avaliação

A pasta `evals/` contém casos de teste para:

* red flags clínicas;
* escalada humana;
* perguntas fora de escopo;
* validação básica do agente.

---

# Considerações de Segurança

O sistema foi desenvolvido como prova de conceito acadêmica.

O agente:

* não substitui atendimento médico;
* não realiza diagnóstico definitivo;
* não prescreve medicamentos;
* orienta atendimento humano em situações críticas.

---

# Integrantes

| Nome                              | RM       |
| --------------------------------- | -------- |
| Matheus Moura da Silva            | RM566782 |
| Kaue Souza Rodrigues              | RM557716 |
| Murylo Silva Amaral               | RM568241 |
| Pedro Henrique Camacho de Alencar | RM568071 |
| Igor Mota Marran                  | RM567823 |

---

# Repositório GitHub

```text
https://github.com/mmoura97/blua-diagnostics-sprint1
```
