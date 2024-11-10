import openai
import os
from dotenv import load_dotenv

load_dotenv()

chave_api = os.getenv('API_KEY')
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append({"role": "user", "content": mensagem})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    
    resposta = response['choices'][0]['message']['content']
    lista_mensagens.append({"role": "assistant", "content": resposta})
    
    return resposta

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem: ")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print("Chatbot:", resposta)
