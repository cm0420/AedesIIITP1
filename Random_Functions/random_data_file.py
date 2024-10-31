import csv
import random
import string
import os

def generate_csv(size):
    # Define o diretório onde os arquivos CSV serão armazenados
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    os.makedirs(data_dir, exist_ok=True)  # Cria o diretório se ele não existir

    data_records = []  # Lista para armazenar os registros de dados

    # Gera os registros de dados com uma chave e valores aleatórios
    for i in range(size):
        key = i + 1  # Incrementa a chave única para cada registro
        data_1 = random.randint(1, 10000)  # Valor inteiro aleatório entre 1 e 10.000
        data_2 = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))  # String aleatória com 1000 caracteres
        data_records.append([key, data_1, data_2])  # Adiciona o registro à lista

    # Nomeia e cria o arquivo CSV original com os dados não ordenados
    random_filename = os.path.join(data_dir, f"random_data_{size}.csv")
    with open(random_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["key", "data1", "data2"])  # Cabeçalhos do CSV
        writer.writerows(data_records)  # Escreve todos os registros de dados

    # Ordena os registros pelo valor 'data1' e salva em outro arquivo CSV
    sorted_filename = os.path.join(data_dir, f"sorted_data_{size}.csv")
    data_records_sorted = sorted(data_records, key=lambda x: x[1])  # Ordena os registros pelo segundo elemento (data1)
    with open(sorted_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["key", "data1", "data2"])  # Cabeçalhos do CSV ordenado
        writer.writerows(data_records_sorted)  # Escreve os registros ordenados
