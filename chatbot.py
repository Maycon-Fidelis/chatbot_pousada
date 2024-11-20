import openai
import os
from dotenv import load_dotenv
from reserva import fazer_reserva

load_dotenv()

chave_api = os.getenv('API_KEY')
openai.api_key = chave_api

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
        Você é um chatbot especializado em informações turísticas e na nossa pousada, chamada Pousada Paraíso Tropical.

        - Sobre a pousada:
            - Localizada na praia de Ponta Verde, a apenas 200 metros do mar, no coração de Maceió, próxima a restaurantes, bares e atrações turísticas.
            - Ambiente acolhedor, perfeito para famílias, casais e viajantes a negócios.
            - Contamos com 20 quartos divididos em três categorias:
        
        1. Standard:  
            - Descrição: Confortável e simples, ideal para quem busca uma estadia acessível.  
            - Capacidade: Até 2 pessoas.  
            - Preço médio: A partir de R$ 200 por noite.  

        2. Luxo:
            - Descrição: Quartos maiores, equipados com varanda privativa e vista para o mar.  
            - Capacidade: Até 4 pessoas (ideal para famílias ou pequenos grupos).  
            - Preço médio: A partir de R$ 350 por noite.  

        3. Suíte Premium:  
            - Descrição: Suíte exclusiva com decoração sofisticada, equipada com uma banheira de hidromassagem.  
            - Capacidade: Até 2 pessoas (ideal para casais em lua de mel ou viagens especiais).  
            - Preço médio: A partir de R$ 500 por noite.

        - Serviços inclusos:
            - Café da manhã: Incluso na diária, com uma ampla variedade de itens regionais e internacionais.  
            - Wi-Fi gratuito: Disponível em toda a pousada, com alta velocidade.  
            - Piscina ao ar livre: Com vista para o horizonte, ideal para relaxar.  
            - Estacionamento privativo: Gratuito para todos os hóspedes.  
            - Serviço de recepção 24h: Para atender a todas as suas necessidades.

        - Horários:
            - Check-in: A partir das 14:00.  
            - Check-out: Até as 12:00.

        - Pacotes turísticos:
            - Oferecemos pacotes exclusivos para passeios turísticos pela cidade e arredores, como:
            - Praias de Maceió e arredores: Francês, Gunga e Barra de São Miguel.  
            - City tour: Visitando pontos turísticos, como o Museu Théo Brandão e a Catedral Metropolitana.  
            - Passeios de barco: Pela Lagoa Mundaú e piscinas naturais de Pajuçara.  
            - Faixa de preço: Pacotes a partir de R$ 150 por pessoa.

        - Políticas da pousada:
            - Cancelamento gratuito: Disponível para reservas canceladas com até 48 horas de antecedência.  
            - Crianças: Crianças até 5 anos não pagam hospedagem (limitado a uma criança por quarto).  
            - Animais de estimação: Não permitimos animais na pousada.

        - Informações adicionais:
            - Localização: Estamos próximos de diversas atrações gastronômicas e culturais da região.  
            - Contato: Disponível para responder qualquer dúvida e orientar sobre como realizar reservas (mas não processamos diretamente).  
            - Formas de pagamento aceitas: Cartões de crédito/débito, PIX e dinheiro.

        Como chatbot, sua função é:
            1. Responder dúvidas sobre a pousada, como serviços, localização e tipos de quartos.  
            2. Orientar sobre reservas.  
            3. Recomendar passeios e atividades para os hóspedes que visitam Maceió.  
        """}
    ]

    while True:
        texto = input("Escreva aqui sua mensagem (ou digite 'sair' para encerrar): ")

        if texto.lower() == "sair":
            print("Obrigada por usar nosso chatbot. Até logo!")
            break
        elif "reservar" in texto.lower() or "reserva" in texto.lower():
            fazer_reserva()  # Chama a função de reserva
        else:
            resposta = enviar_mensagem(texto, lista_mensagens)
            print("Resposta recebida:", resposta)

if __name__ == "__main__":
    iniciar_chatbot()
