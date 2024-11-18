import csv
import pandas as pd
from datetime import datetime

def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)

def verificar_disponibilidade(reservas, data_entrada, data_saida, tipo_quarto):
    data_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
    data_saida = datetime.strptime(data_saida, '%Y-%m-%d')

    reservas_filtradas = reservas[(reservas['TipoQuarto'] == tipo_quarto) & (reservas['StatusReserva']) == 'Confirmada']

    for _, reservas in reservas_filtradas.iterrows():
        reserva_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
        reserva_saida = datetime.strptime(data_saida, '%Y-%m-%d')

        if(reserva_entrada < reserva_saida) and (data_saida > reserva_entrada):
            return False
    return True

def adicionar_reserva(caminho_csv, nova_reserva):
    reserva = carregar_dados(caminho_csv)
    reservas = pd.concat([reserva, pd.DataFrame([nova_reserva])], ignore_index=True)
    reservas.to_csv(caminho_csv, index=False)

def atualizar_status_reserva(caminho_csv,reserva_id,novo_status):
    reservas = carregar_dados(caminho_csv)
    reservas.loc[reservas['ReservaID'] == str(reserva_id), 'StatusReserva'] = novo_status
    reservas.to_csv(caminho_csv,index=False)

def consultar_reservas(reservas, data=None, tipo_quarto=None):
    if data:
        data = datetime.strptime(data, '%Y-%m-%d')
        reservas = reservas[(reservas['DataEntrada'] <= data.strftime('%Y-%m-%d')) & (reservas['DataSaida' >= data.strftime('%Y-%m-%d')])]
    if tipo_quarto:
        reservas = reservas[reservas['TipoQuarto'] == tipo_quarto]
    return reservas

def cancelar_reserva(caminho_csv,reserva_id):
    reservas = carregar_dados(caminho_csv)
    reservas = reservas[reservas['ReservaID'] != str(reserva_id)]
    reservas.to_csv(caminho_csv, index=False)