import os
import sys
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Configuração para evitar erros de codificação no Windows com emojis
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Instanciando o Agente Analista com as Ferramentas (Tools)
analista_financeiro = Agent(
    name="Analista de Wall Street",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[
        DuckDuckGoTools(), 
        YFinanceTools(enable_stock_price=True, enable_analyst_recommendations=True, enable_stock_fundamentals=True, enable_company_info=True)
    ],
    description="Você é um Analista Financeiro de Wall Street muito experiente e objetivo.",
    instructions=[
        "Sempre use as ferramentas YFinanceTools para buscar o preço atual da ação e informações fundamentais da empresa.",
        "Sempre use a ferramenta DuckDuckGoTools para buscar as últimas notícias sobre a empresa para dar contexto atual.",
        "Organize seu relatório em tópicos: 1. Dados da Ação, 2. Notícias Recentes, 3. Conclusão/Recomendação.",
        "Responda sempre em português.",
        "Utilize Markdown para formatar tabelas e destaques no texto."
    ],
    markdown=True
)

if __name__ == "__main__":
    print("🚀 Iniciando a Interface Interativa Nativa do Agno (CLI)...")
    # cli_app() inicia um chat interativo direto no terminal com histórico e logs bonitos das ferramentas
    analista_financeiro.cli_app(stream=True)
