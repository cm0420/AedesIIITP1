class SequentialNode:
    def __initial__(self,key,data1,data2):
        # Inicializa um nó com uma chave e dois dado
        self.key= key
        self.data1= data1
        self.data2= data2
        
class SequentialFList:
    # Inicializa uma lista vazia para armazenar os nós
    def __init__(self):
        self.tree= []
    
    def insert(self, key, data1, data2):
          # Cria um novo nó com a chave e os dados fornecidos
        node = SequentialNode(key, data1, data2)
        # Adiciona o nó à lista (tree)
        self.tree.append(node)
    
    def search_n_count(self, key):
         # Enumera cada nó da lista, com 'comparisons' contando o índice + 1
        for comparisons, node in enumerate(self.tree, start=1):
              # Verifica se a chave do nó atual é igual à chave de busca
            if node.key == key:
                # Se encontrada, retorna o nó e a quantidade de comparações feitas
                return node, comparisons
              # Se não encontrada, retorna None e o número total de comparações feitas
            return None, comparisons
             # comparisons será o comprimento de self.tree se não encontrado