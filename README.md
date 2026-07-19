# Analista Financeiro AI com Agno

Este projeto é um agente de inteligência artificial criado usando o framework [Agno](https://github.com/agno-ai/agno). Ele atua como um experiente Analista Financeiro de Wall Street, capaz de buscar preços de ações, fundamentos de empresas e notícias recentes para fornecer relatórios detalhados.

## 🚀 Tecnologias

- **Agno**: Framework para construção de agentes AI.
- **DuckDuckGo Tools**: Utilizado para buscar as últimas notícias e dar contexto atualizado.
- **YFinance Tools**: Utilizado para buscar dados financeiros e cotações de ações.
- **FastAPI / Uvicorn**: Para servir a interface do agente web.

## 🛠️ Como instalar

### Docker (Recomendado)

1. Certifique-se de que o Docker está instalado e rodando.
2. Crie seu arquivo `.env` com a sua `GOOGLE_API_KEY` conforme as instruções abaixo.
3. Na raiz do projeto, execute:
   ```bash
   docker-compose up --build
   ```
4. O servidor web estará disponível em `http://localhost:7777`.

Para parar a execução, aperte `Ctrl + C` no terminal ou rode `docker-compose down`.

### Instalação Nativa
1. Clone o repositório ou baixe os arquivos.
2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz do projeto (use o arquivo `.env.example` como base) e insira sua chave da API do Google:
   ```env
   GOOGLE_API_KEY=sua_chave_aqui
   ```

## 🎮 Como usar

### CLI (Terminal)

Para conversar com o agente diretamente no terminal, execute:
```bash
python playground.py
```

### Servidor Web (Agent UI)

Para rodar o agente através de uma interface gráfica web (Agent UI), inicie o servidor:
```bash
python serve.py
```
O servidor estará rodando em `http://localhost:7777`.