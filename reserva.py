import csv
from datetime import datetime

ARQUIVO_RESERVAS = "reservas.csv"

CAPACIDADE_QUARTOS = {
    "Standard": 10,
    "Luxo": 6,
    "Suíte Premium": 4
}

def verificar_disponibilidade(data_checkin, data_checkout, tipo_quarto):
    """Verifica se as datas estão disponíveis para o tipo de quarto solicitado e respeita o limite máximo de reservas."""
    try:
        with open(ARQUIVO_RESERVAS, mode="r") as arquivo_csv:
            reader = csv.DictReader(arquivo_csv)
            reservas_ativas = 0
            nova_data_checkin = datetime.strptime(data_checkin, "%d-%m-%Y")
            nova_data_checkout = datetime.strptime(data_checkout, "%d-%m-%Y")

            for linha in reader:
                if linha["Tipo do Quarto"] == tipo_quarto:
                    data_checkin_existente = datetime.strptime(linha["Data Check-in"], "%d-%m-%Y")
                    data_checkout_existente = datetime.strptime(linha["Data Check-out"], "%d-%m-%Y")

                    if not (nova_data_checkout <= data_checkin_existente or nova_data_checkin >= data_checkout_existente):
                        reservas_ativas += 1

                    if reservas_ativas >= CAPACIDADE_QUARTOS[tipo_quarto]:
                        return False
        return True
    except FileNotFoundError:
        return True
    except Exception as e:
        print(f"Erro ao verificar disponibilidade: {e}")
        return False

def salvar_reserva(nome, telefone, email, tipo_quarto, data_checkin, data_checkout, num_pessoas):
    """Salva os dados da reserva no arquivo CSV."""
    try:
        with open(ARQUIVO_RESERVAS, mode="a", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)

            if arquivo_csv.tell() == 0:
                writer.writerow(["Nome", "Telefone", "E-mail", "Tipo do Quarto", "Data Check-in", "Data Check-out", "Número de Pessoas", "Data da Reserva"])
            
            writer.writerow([
                nome, 
                telefone, 
                email, 
                tipo_quarto, 
                data_checkin, 
                data_checkout, 
                num_pessoas, 
                datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            ])
    except Exception as e:
        print(f"Erro ao salvar a reserva: {e}")

def fazer_reserva():
    """Fluxo para registrar uma reserva."""
    print("Vamos verificar a disponibilidade antes de continuar com sua reserva.")
    
    tipo_quarto = input("Qual o tipo de quarto? (Standard, Luxo, Suíte Premium): ")
    data_checkin = input("Data de check-in (formato DD-MM-AAAA): ")
    data_checkout = input("Data de check-out (formato DD-MM-AAAA): ")

    if verificar_disponibilidade(data_checkin, data_checkout, tipo_quarto):
        print("O quarto está disponível! Vamos prosseguir com a sua reserva.")
        nome = input("Qual é o seu nome? ")
        telefone = input("Qual é o seu número de telefone? ")
        email = input("Qual é o seu e-mail? ")
        num_pessoas = input("Número de pessoas: ")

        try:
            salvar_reserva(nome, telefone, email, tipo_quarto, data_checkin, data_checkout, num_pessoas)
            print("Reserva realizada com sucesso! Você receberá um e-mail de confirmação em breve.")
        except Exception as e:
            print(f"Ocorreu um erro ao registrar sua reserva: {e}")
    else:
        print(f"Desculpe, as datas solicitadas estão indisponíveis ou o tipo de quarto {tipo_quarto} está lotado.")

if __name__ == "__main__":
    fazer_reserva()