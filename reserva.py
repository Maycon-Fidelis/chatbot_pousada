import csv
from datetime import datetime

ARQUIVO_CSV = "reservas.csv"

def carregar_reservas():
    reservas = []
    with open(ARQUIVO_CSV, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            reservas.append(row)
    return reservas

def salvar_reservas(reservas):
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["ReservaID", "HospedeNome", "HospedeContato", "DataEntrada", "DataSaida", "TipoQuarto", "StatusReserva"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reservas)

def verificar_disponibilidade(data_entrada, data_saida, tipo_quarto):
    reservas = carregar_reservas()
    for reserva in reservas:
        if reserva["TipoQuarto"] == tipo_quarto and reserva["StatusReserva"] == "Confirmada":
            if not (data_saida <= reserva["DataEntrada"] or data_entrada >= reserva["DataSaida"]):
                return False
    return True

def adicionar_reserva(nome, contato, data_entrada, data_saida, tipo_quarto):
    reservas = carregar_reservas()
    nova_reserva = {
        "ReservaID": str(len(reservas) + 1),
        "HospedeNome": nome,
        "HospedeContato": contato,
        "DataEntrada": data_entrada,
        "DataSaida": data_saida,
        "TipoQuarto": tipo_quarto,
        "StatusReserva": "Confirmada"
    }
    reservas.append(nova_reserva)
    salvar_reservas(reservas)

def cancelar_reserva(reserva_id):
    reservas = carregar_reservas()
    for reserva in reservas:
        if reserva["ReservaID"] == reserva_id:
            reserva["StatusReserva"] = "Cancelada"
    salvar_reservas(reservas)
