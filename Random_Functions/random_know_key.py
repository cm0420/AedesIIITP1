import random

def get_random_keys(records, num_keys=15):
    unique_keys = set(record[0] for record in records) # Cria um conjunto de chaves únicas a partir da lista de registros
    return random.sample(unique_keys, num_keys) # Seleciona um subconjunto aleatório de chaves com base no número desejado