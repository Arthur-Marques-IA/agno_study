import sys
from agno.os import AgentOS
from agno.os.interfaces.agui import AGUI

# Importamos o agente configurado no playground.py
from playground import analista_financeiro

# Configuração para evitar erros de codificação no Windows com emojis
sys.stdout.reconfigure(encoding='utf-8')

# Configura o AgentOS com a interface AGUI para comunicação com o Agent UI frontend
agent_os = AgentOS(
    agents=[analista_financeiro],
    interfaces=[AGUI(agent=analista_financeiro)],
)

app = agent_os.get_app()

if __name__ == "__main__":
    print("🚀 Iniciando o servidor AgentOS para o Agent UI em http://localhost:7777 ...")
    agent_os.serve(app="serve:app", reload=True)
