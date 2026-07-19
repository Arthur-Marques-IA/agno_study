FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o requirements primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Expõe a porta que o servidor AgentOS utiliza
EXPOSE 7777

# Comando padrão para rodar a aplicação web
CMD ["python", "serve.py"]
