import anthropic
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Pegar chave do ambiente (seguro!)
API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not API_KEY:
    print("❌ ERRO: Chave API não encontrada no arquivo .env")
    exit()

# Criar cliente
client = anthropic.Anthropic(api_key=API_KEY)

print("🤖 Perguntando ao Claude...\n")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": "Me diga um fato curioso sobre programação."
        }
    ]
)

resposta = message.content[0].text
printf("Claude respondeu:\n{resposta}\n")import anthropic

