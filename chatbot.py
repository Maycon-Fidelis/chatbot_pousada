import openai
import os
from dotenv import load_dotenv
from reserva import fazer_reserva
import time

load_dotenv()

chave_api = os.getenv('API_KEY')
openai.api_key = chave_api

def analisar_intencao(mensagem):
    prompt = f"""
    Você é um assistente que deve classificar a intenção de uma mensagem.
    Analise a seguinte mensagem e responda apenas com uma das opções:
    - 'reserva': se o usuário está solicitando realizar uma reserva ou informações diretamente relacionadas a iniciar uma reserva.
    - 'informacao': se o usuário está pedindo informações gerais ou fazendo uma pergunta.

    Mensagem do usuário:
    "{mensagem}"
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
        
    intencao = response['choices'][0]['message']['content'].strip().lower()
    return intencao

def enviar_mensagem(mensagem, lista_mensagens=[]):
    """Envia mensagem para a API da OpenAI e retorna a resposta."""
    lista_mensagens.append({"role": "user", "content": mensagem})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )
    
    resposta = response['choices'][0]['message']['content']
    lista_mensagens.append({"role": "assistant", "content": resposta})
    
    return resposta

def iniciar_chatbot():
    """Inicia o chatbot e gerencia as interações do usuário."""
    lista_mensagens = [
        {"role": "system", "content": """
        Você é um chatbot especializado em informações turísticas e na pousada "Pousada Paraíso Tropical".

        Funções principais:
        1. Respostas a perguntas frequentes:  
        - Tipos de quartos, capacidade, preços e disponibilidade.  
        - Políticas de cancelamento, horários de check-in/check-out e serviços inclusos.  
        - Informações sobre localização e formas de contato.  

        2. Auxílio na realização de reservas:  
        - Solicitar informações como:  
            - Datas de entrada e saída.  
            - Tipo de quarto desejado.  
            - Número de pessoas e dados de contato.  
        - Confirmar disponibilidade com base nas informações fornecidas.  

        3. Recomendações turísticas:  
        - Sugerir praias, restaurantes e atividades culturais em Maceió e arredores.  
        - Oferecer detalhes sobre pacotes turísticos disponíveis.  

        Sobre a pousada:
        - Localização: Praia de Ponta Verde, a 200m do mar, no coração de Maceió.  
        - Ambiente: Acolhedor, ideal para famílias, casais e viajantes a negócios.  
        - Quartos disponíveis (20 no total):  
        1. Standard:  
            - Descrição: Simples e confortável, ideal para estadias acessíveis.  
            - Capacidade: Até 2 pessoas.  
            - Preço: A partir de R$ 200/noite.  
            - Quantidade: 10 quartos.  
        2. Luxo:  
            - Descrição: Amplo, com varanda privativa e vista para o mar.  
            - Capacidade: Até 4 pessoas.  
            - Preço: A partir de R$ 350/noite.  
            - Quantidade: 6 quartos.  
        3. Suíte Premium:  
            - Descrição: Sofisticada, com hidromassagem.  
            - Capacidade: Até 2 pessoas (ideal para ocasiões especiais).  
            - Preço: A partir de R$ 500/noite.  
            - Quantidade: 4 quartos.  

        Serviços inclusos:
        - Café da manhã: Variado, com itens regionais e internacionais.  
        - Wi-Fi: Gratuito e de alta velocidade.  
        - Piscina: Com vista para o horizonte.  
        - Estacionamento privativo: Gratuito.  
        - Recepção 24h: Pronta para atender às necessidades dos hóspedes.

        Políticas da pousada:
        - Cancelamento gratuito: Para reservas canceladas até 48 horas antes do check-in.  
        - Check-in: A partir das 14h.  
        - Check-out: Até as 12h.  
        - Crianças: Uma criança até 5 anos não paga hospedagem por quarto.  
        - Animais: Não permitimos animais de estimação.  

        Pacotes turísticos oferecidos:  
        - Praias de Maceió e arredores: Francês, Gunga e Barra de São Miguel.  
        - City tour: Museu Théo Brandão, Catedral Metropolitana e outros pontos turísticos.  
        - Passeios de barco: Lagoa Mundaú e piscinas naturais de Pajuçara.  
        - Preços: A partir de R$ 150 por pessoa.  

        Dicas turísticas em Maceió:
        1. Praias: Pajuçara, Francês, Gunga.  
        2. Restaurantes: Massarella, Imperador dos Camarões, Parmegianno.  
        3. Cultura: Museu Théo Brandão, Catedral Metropolitana.  

        Como chatbot, você deve ser amigável, claro e objetivo, sempre guiando os visitantes na busca por informações ou na tomada de decisões sobre a estadia e atividades em Maceió.
        """
        }
    ]

    while True:
        texto = input("Escreva aqui sua mensagem (ou digite 'sair' para encerrar): ")

        if texto.lower() == "sair":
            print("Obrigada por usar nosso chatbot. Até logo!")
            break

        intencao = analisar_intencao(texto)

        if intencao == "'reserva'":
            print("Iniciando o processo de reserva...")
            fazer_reserva()
        else:
            resposta = enviar_mensagem(texto, lista_mensagens)
            print("Resposta recebida:", resposta)

if __name__ == "__main__":
    iniciar_chatbot()