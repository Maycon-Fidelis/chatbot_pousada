import openai
import os
import json
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

def iniciar_chatbot():
    lista_mensagens = [
        {"role": "system", "content": """
            Você é um chatbot de reservas e informações turísticas sobre Maceió. 
            Quando alguém desejar fazer uma reserva, responda no seguinte formato JSON:
            {
              "action": "reserva",
              "data_entrada": "<data>",
              "data_saida": "<data>",
              "tipo_quarto": "<tipo>",
              "status": "<disponível/não disponível>"
            }
            
            Para informações turísticas, apenas forneça a lista de pontos turísticos.
        """}
    ]

    while True:
        texto = input("Escreva aqui sua mensagem: ")

        if texto.lower() == "sair":
            break
        else:
            resposta = enviar_mensagem(texto, lista_mensagens)

            try:
                dados = json.loads(resposta)

                if dados["action"] == "reserva":
                    print("Log de reserva:")
                    print(f"Data de Entrada: {dados.get('data_entrada')}")
                    print(f"Data de Saída: {dados.get('data_saida')}")
                    print(f"Tipo de Quarto: {dados.get('tipo_quarto')}")
                    print(f"Status: {dados.get('status')}")
                else:
                    print("Resposta não relacionada a reserva:", resposta)

            except json.JSONDecodeError:
                print("Resposta recebida (não está em formato JSON):", resposta)

iniciar_chatbot()
