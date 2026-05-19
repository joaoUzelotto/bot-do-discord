from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def perguntar_ia(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um bot divertido, amigável e gamer do Discord."
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ]
        )

        return resposta.choices[0].message.content

    except Exception as e:
        print("Erro na IA:", e)
        return "Deu erro na IA 😢"