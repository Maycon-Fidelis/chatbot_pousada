import csv
import pandas as pd
from datetime import datetime

def carregar_reservas(caminho_csv):
    return pd.read_csv(caminho_csv)

def verificar_disponibilidade(reservas, data_entrada, data_saida, tipo_quarto):
    data_entrada = datetime.strptime(data_entrada, '%Y-%m-%d')
    data_saida = datetime.strptime(data_saida, '%Y-%m-%d')

    # Filtra as reservas confirmadas do tipo especificado
    reservas_filtradas = reservas[(reservas['TipoQuarto'] == tipo_quarto) & 
                                  (reservas['StatusReserva'] == 'Confirmada')]

    # Verifica se há conflito de datas
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

def atualizar_status_reserva(caminho_csv, reserva_id, novo_status):
    reservas = carregar_reservas(caminho_csv)
    reservas.loc[reservas['ReservaID'] == str(reserva_id), 'StatusReserva'] = novo_status
    reservas.to_csv(caminho_csv, index=False)

def consultar_reservas(reservas, data=None, tipo_quarto=None):
    if data:
        data = datetime.strptime(data, '%Y-%m-%d')
        reservas = reservas[(reservas['DataEntrada'] <= data.strftime('%Y-%m-%d')) &
                            (reservas['DataSaida'] >= data.strftime('%Y-%m-%d'))]
    if tipo_quarto:
        reservas = reservas[reservas['TipoQuarto'] == tipo_quarto]
    return reservas

def remover_reserva(caminho_csv, reserva_id):
    reservas = carregar_reservas(caminho_csv)
    reservas = reservas[reservas['ReservaID'] != str(reserva_id)]
    reservas.to_csv(caminho_csv, index=False)

#CÓDIGO ABAIXO TESTANDO OS CÒDIGOS DE RESERVA

# Caminho para o CSV de exemplo
caminho_csv = 'dados_pousada.csv'

# Carregar reservas para verificar a leitura do CSV
reservas = carregar_reservas(caminho_csv)
print("Reservas carregadas:")
print(reservas)

# Teste de verificar_disponibilidade
data_entrada = '2024-11-02'
data_saida = '2024-11-04'
tipo_quarto = 'Deluxe'
disponivel = verificar_disponibilidade(reservas, data_entrada, data_saida, tipo_quarto)
print(f"\nDisponibilidade de {tipo_quarto} entre {data_entrada} e {data_saida}: {'Disponível' if disponivel else 'Indisponível'}")

# Teste de adicionar_reserva
nova_reserva = {
    'ReservaID': '3',
    'HospedeNome': 'Carlos Pereira',
    'HospedeContato': '77777-7777',
    'DataEntrada': '2024-11-12',
    'DataSaida': '2024-11-14',
    'TipoQuarto': 'Standard',
    'StatusReserva': 'Confirmada',
    'NumeroPessoas': '1',
    'ValorTotal': '250.00',
    'DataReserva': '2024-11-01',
    'Notas': 'Reserva especial'
}
adicionar_reserva(caminho_csv, nova_reserva)
print("\nReserva adicionada.")
print(pd.read_csv(caminho_csv))

# Teste de atualizar_status_reserva
atualizar_status_reserva(caminho_csv, '3', 'Cancelada')
print("\nStatus da reserva atualizado:")
print(pd.read_csv(caminho_csv))

# Teste de consultar_reservas
data_consulta = '2024-11-12'
tipo_quarto_consulta = 'Standard'
consultas = consultar_reservas(reservas, data_consulta, tipo_quarto_consulta)
print(f"\nConsultando reservas para {tipo_quarto_consulta} em {data_consulta}:")
print(consultas)

# Teste de remover_reserva
remover_reserva(caminho_csv, '3')
print("\nReserva removida.")
print(pd.read_csv(caminho_csv))
