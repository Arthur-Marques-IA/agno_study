FROM node:20-alpine

WORKDIR /app

# Instala o pnpm globalmente
RUN npm install -g pnpm

# Copia os arquivos de dependência
COPY package.json pnpm-lock.yaml* ./

# Instala as dependências
RUN pnpm install

# Copia o restante dos arquivos do frontend
COPY . .

# Variável necessária para o Next.js liberar o acesso fora do container
ENV HOSTNAME 0.0.0.0
EXPOSE 3000

# Inicia em modo de desenvolvimento
CMD ["pnpm", "dev"]
