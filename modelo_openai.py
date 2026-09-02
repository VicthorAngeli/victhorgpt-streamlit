import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

mensagens = [
    SystemMessage(content="Responda as perguntas de forma curta.")
]

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY"),
)

if __name__ == "__main__":
    mensagens_humano = input("Digite sua mensagem: ")
    conversa = mensagens + [HumanMessage(content=mensagens_humano)]

    resposta = modelo.invoke(conversa)

    print(resposta)
    print(type(resposta))
    print(resposta.content)
    print(resposta.type)