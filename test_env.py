from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("DATABASE_KEY")
print("String de conexão encontrada:", database_url is not None)
if database_url:
    print("Primeiros 20 caracteres da string:", database_url[:20] + "...") 