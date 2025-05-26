# Data Engineer - API BTC

Este projeto é um sistema completo para coleta, processamento e visualização de dados do Bitcoin, utilizando uma arquitetura moderna com pipeline de dados, agente inteligente e dashboard interativo.

## 🏗️ Estrutura do Projeto

O projeto está organizado em três componentes principais:

### 1. Pipeline (`/Pipeline`)
- Responsável pela coleta e processamento de dados do Bitcoin
- Implementado em `app.py`
- Coleta dados em tempo real da API do Bitcoin
- Processa e armazena os dados em um banco de dados PostgreSQL

### 2. Agente (`/Agente`)
- Implementa um agente inteligente usando a biblioteca Agno
- Utiliza o modelo Groq para processamento de linguagem natural
- Permite consultas inteligentes aos dados do Bitcoin
- Implementado em `agente.py`

### 3. Dashboard (`/Dashboard`)
- Interface visual para análise dos dados
- Implementado em `appdash.py`
- Apresenta visualizações interativas dos dados do Bitcoin
- Permite análise temporal e comparações

## 🚀 Tecnologias Utilizadas

- Python 3.x
- PostgreSQL
- Agno Framework
- Groq API
- Dash/Plotly (para visualizações)
- dotenv (para gerenciamento de variáveis de ambiente)

## ⚙️ Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [https://github.com/Gabriel-Rosatto-Dantas/Data-Enginner---API-BTC]
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
# API Keys
GROQ_API_KEY=sua_chave_aqui
AGNO_API_TOKEN=sua_chave_aqui

# PostgreSQL
POSTGRES_HOST=seu_host
POSTGRES_PORT=5432
POSTGRES_DB=seu_banco
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_SCHEMA=public
```

## 🎯 Como Usar

### Pipeline
```bash
cd Pipeline
python app.py
```

### Agente
```bash
cd Agente
python agente.py
```

### Dashboard
```bash
cd Dashboard
python appdash.py
```

## 📊 Funcionalidades

- Coleta automática de dados do Bitcoin
- Processamento e armazenamento em banco de dados
- Consultas inteligentes via agente
- Visualizações interativas no dashboard
- Análise temporal de preços
- Indicadores técnicos
