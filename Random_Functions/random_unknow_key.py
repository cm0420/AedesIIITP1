import random

def generate_unknown_keys(data_records, count=15):
    # Cria um conjunto de chaves existentes a partir dos registros de dados
    existing_keys = {record[0] for record in data_records}
    
    # Encontra a chave máxima para começar a gerar novas chaves a partir de um intervalo mais alto
    max_key = max(existing_keys)
    
    # Inicializa uma lista para armazenar chaves desconhecidas (novamente geradas)
    unknown_keys = []
    
    # Gera chaves desconhecidas únicas até atingir a quantidade desejada
    while len(unknown_keys) < count:
        # Gera uma nova chave dentro de um intervalo acima da chave máxima existente
        new_key = random.randint(max_key + 1, max_key + 1000)
        
        # Garante que a nova chave seja única e não esteja nas chaves existentes ou desconhecidas
        if new_key not in existing_keys and new_key not in unknown_keys:
            unknown_keys.append(new_key)
    
    return unknown_keys