from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.postgres import PostgresTools
from dotenv import load_dotenv
import os

load_dotenv()

# Inicialização do PostgresTools com os detalhes da conexão
postgres_tools = PostgresTools(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    db_name=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    table_schema=os.getenv("POSTGRES_SCHEMA"),
)

# Criação do agente com o PostgresTools
agent = Agent(tools=[postgres_tools],
              model=Groq(id="llama-3.3-70b-versatile",
                         api_key=os.getenv("AGNO_API_TOKEN")))

agent.print_response("Fale todas as tabelas do banco de dados", markdown=True)

agent.print_response("""
Faça uma query para pegar todas as cotações de bitcoin na tabela bitcoin_dados
""")

agent.print_response("""
Faça uma análise super complexa sobre o bitcoin usando os dados da tabela bitcoin_dados
""")