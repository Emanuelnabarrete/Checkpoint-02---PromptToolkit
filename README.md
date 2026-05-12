
# Prompt Toolkit

Projeto desenvolvido para o Checkpoint 02 da disciplina **Prompt Engineering & Artificial Intelligence** da FIAP.

O objetivo do projeto é comparar diferentes técnicas de Prompt Engineering utilizando um modelo LLM local via Ollama, analisando métricas como acurácia, tempo de resposta, quantidade de tokens e consistência.

---

# Técnicas implementadas

O toolkit executa automaticamente as seguintes técnicas:

* Zero-Shot Prompting
* Few-Shot Prompting
* Chain-of-Thought (CoT)
* Role Prompting

---

# Tecnologias utilizadas

* Python 3.10+
* Ollama
* Modelo `gpt-oss:120b`
* pandas
* matplotlib
* tiktoken
* requests

---

# Estrutura do projeto

```bash id="9l9xkh"
prompt-toolkit/
├── main.py
├── requirements.txt
├── .env
├── src/
├── data/
├── prompts/
└── output/
```

---

# Como executar

## 1. Clonar o repositório

```bash id="9jxyh8"
git clone <url-do-repositorio>
cd prompt-toolkit
```

---

## 2. Criar ambiente virtual

```bash id="bj4v43"
python -m venv venv
```

---

## 3. Ativar ambiente virtual

### Windows

```bash id="22ulom"
venv\Scripts\activate
```

```

---

## 4. Instalar dependências

```bash id="dgn9tk"
pip install -r requirements.txt
```

---

# Configuração do Ollama

Instalar Ollama:

https://ollama.com

Baixar o modelo:

```bash id="0qvjbe"
ollama pull gpt-oss:120b
```

Iniciar o servidor:

```bash id="pq1cjq"
ollama serve
```

---

# Arquivo .env

Criar um arquivo `.env` na raiz do projeto:

```env id="u0jlwm"
OLLAMA_HOST=http://localhost:11434
MODEL=gpt-oss:120b
```

---

# Executar o projeto

```bash id="gkq01f"
python main.py
```

---

# Saídas geradas

O sistema gera automaticamente:

* `results.csv`
* `temperature.csv`
* `recommendation.txt`
* gráficos comparativos em `output/charts`

Os gráficos incluem:

* acurácia por técnica
* consumo médio de tokens
* tempo médio de resposta
* consistência por temperatura

---

# Objetivo acadêmico

Este projeto tem como objetivo aplicar conceitos de Prompt Engineering na prática, comparando diferentes estratégias de prompting e avaliando seus resultados utilizando métricas quantitativas.

---

# Integrantes

* Emanuel Nabarrete 
* Luiz Eduardo
* Eduardo Luiz
* Miguel Bezerra
* Lucas Mota
