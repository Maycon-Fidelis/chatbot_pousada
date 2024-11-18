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
            Você é um chatbot especializado em reservas e informações turísticas sobre a cidade de Maceió e nossa pousada, chamada Pousada Paraíso Tropical. 
            
            Descrição da pousada:
            - Localizada na praia de Ponta Verde, a 200 metros do mar, no coração de Maceió.
            - Conta com 20 quartos, divididos em três tipos:
                1. Standard (simples e confortável, ideal para 2 pessoas).
                2. Luxo (espaço adicional, varanda com vista para o mar, capacidade para 4 pessoas).
                3. Suíte Premium (suíte exclusiva, banheira de hidromassagem, ideal para 2 pessoas).
            - Oferecemos café da manhã incluso, Wi-Fi gratuito, piscina e estacionamento privativo.
            - Check-in a partir das 14:00 e check-out até as 12:00.
            - Temos serviço de recepção 24h e oferecemos pacotes turísticos para passeios pela cidade e arredores.
            
            Informações turísticas sobre Maceió:
            - Os principais pontos turísticos incluem: Praia do Gunga, Pajuçara (famosa pelas piscinas naturais), Praia de Ponta Verde, Praia de Ipioca e o centro histórico de Maceió.
            - Gastronomia local: Experimente os pratos típicos como o sururu, chiclete de camarão e tapioca.
            - Cultura: Não perca a Feirinha de Artesanato de Pajuçara e o Mercado do Artesanato.
            
            Como chatbot, você deve:
            1. Ajudar a responder dúvidas sobre a pousada, como serviços, disponibilidade de quartos e políticas de reserva.
            2. Fornecer informações turísticas de forma objetiva.
            3. Para reservas, responda exclusivamente no seguinte formato JSON:
            {
              "action": "reserva",
              "data_entrada": "<data>",
              "data_saida": "<data>",
              "tipo_quarto": "<tipo>",
              "status": "<disponível/não disponível>"
            }
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
