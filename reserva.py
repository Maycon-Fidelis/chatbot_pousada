import pandas as pd
from datetime import datetime

def carregar_reservas(caminho_csv):
    return pd.read_csv(caminho_csv)

def verificar_disponibilidade(reservas, data_entrada, data_saida, tipo_quarto):
    data_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
    data_saida = datetime.strptime(data_saida, '%Y-%m-%d')
    reservas_filtradas = reservas[(reservas['TipoQuarto'] == tipo_quarto) & 
                                  (reservas['StatusReserva'] == 'Confirmada')]
    for _, reserva in reservas_filtradas.iterrows():
        reserva_entrada = datetime.strptime(reserva['DataEntrada'], '%Y-%m-%d')
        reserva_saida = datetime.strptime(reserva['DataSaida'], '%Y-%m-%d')
        if (data_entrada < reserva_saida) and (data_saida > reserva_entrada):
            return False
    return True

def adicionar_reserva(caminho_csv, nova_reserva):
    reservas = carregar_reservas(caminho_csv)
    reservas = pd.concat([reservas, pd.DataFrame([nova_reserva])], ignore_index=True)
    reservas.to_csv(caminho_csv, index=False)
