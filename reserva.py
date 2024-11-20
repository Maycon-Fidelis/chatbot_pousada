import csv
from datetime import datetime

ARQUIVO_RESERVAS = "reservas.csv"

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
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
    except Exception as e:
        print(f"Erro ao salvar a reserva: {e}")

def fazer_reserva():
    """Fluxo para registrar uma reserva."""
    print("Vamos realizar a sua reserva!")
    
    nome = input("Qual é o seu nome? ")
    telefone = input("Qual é o seu número de telefone? ")
    email = input("Qual é o seu e-mail? ")
    tipo_quarto = input("Qual o tipo de quarto? (Standard, Luxo, Suíte Premium) ")
    data_checkin = input("Data de check-in (formato AAAA-MM-DD): ")
    data_checkout = input("Data de check-out (formato AAAA-MM-DD): ")
    num_pessoas = input("Número de pessoas: ")

    try:
        salvar_reserva(nome, telefone, email, tipo_quarto, data_checkin, data_checkout, num_pessoas)
        print("Reserva realizada com sucesso! Você receberá um e-mail de confirmação em breve.")
    except Exception as e:
        print(f"Ocorreu um erro ao registrar sua reserva: {e}")

if __name__ == "__main__":
    fazer_reserva()
