import csv
from datetime import datetime

# Caminho do arquivo CSV
ARQUIVO_RESERVAS = "reservas.csv"

# Função para salvar reserva
def salvar_reserva(nome, tipo_quarto, data_checkin, data_checkout, num_pessoas):
    """Salva os dados da reserva no arquivo CSV."""
    # Certifique-se de criar o arquivo com cabeçalhos se ele não existir
    try:
        with open(ARQUIVO_RESERVAS, mode="a", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            
            # Escrever cabeçalhos, se necessário
            if arquivo_csv.tell() == 0:
                writer.writerow(["Nome", "Tipo do Quarto", "Data Check-in", "Data Check-out", "Número de Pessoas", "Data da Reserva"])
            
            # Salvar a reserva
            writer.writerow([nome, tipo_quarto, data_checkin, data_checkout, num_pessoas, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    except Exception as e:
        print(f"Erro ao salvar a reserva: {e}")
