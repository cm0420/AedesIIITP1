class AVLNode:
    def __init__(self, key, data1, data2):
        # Inicializa um nó da árvore AVL com uma chave e dois dados
        self.key = key        
        self.data1 = data1    
        self.data2 = data2    
        self.left = None      
        self.right = None     
        self.height = 1       

class AVLTree:
    def __init__(self):
        # Inicializa a árvore AVL com a raiz vazia
        self.root = None

    def insert(self, key, data1, data2):
        # Insere um novo nó na árvore AVL
        self.root = self._insert_node(self.root, key, data1, data2)

    def _insert_node(self, node, key, data1, data2):
        if not node:
            return AVLNode(key, data1, data2)

        if key < node.key:
            node.left = self._insert_node(node.left, key, data1, data2)
        elif key > node.key:
            node.right = self._insert_node(node.right, key, data1, data2)
        else:
            return node

        # Atualiza a altura do no
        node.height = self._update_height(node)
        
        # OLha balanceamento e realiza as rotações necessárias
        return self._balance_tree(node, key)

    def _update_height(self, node):
        # Atualiza a altura do nó
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_height(self, node):
        # Retorna a altura do nó ou 0 se não existir
        return node.height if node else 0

    def _get_balance(self, node):
        # Calcula o fator de balanceamento do nó
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y):
        # Realiza uma rotação à direita
        x = y.left
        y.left = x.right
        x.right = y
        y.height = self._update_height(y)
        x.height = self._update_height(x)
        return x

    def _rotate_left(self, x):
        # Realiza uma rotação à esquerda
        y = x.right
        x.right = y.left
        y.left = x
        x.height = self._update_height(x)
        y.height = self._update_height(y)
        return y

    def _balance_tree(self, node, key):
        # Realiza o balanceamento da árvore
        balance = self._get_balance(node)

        # trata usando os 4 casos se necessário 
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)  # Caso 1- esquerda-esquerda
            else:
                node.left = self._rotate_left(node.left)  # Caso 2-  esquerda-direita
                return self._rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)  # Caso 3-  direita-direita
            else:
                node.right = self._rotate_right(node.right)  # Caso 4-  direita-esquerda
                return self._rotate_left(node)

        return node  # Retorna o nó  após o balanceamento

    def search_with_count(self, key):
        # busca pela chave e conta comparações
        return self._search_node(self.root, key, 0)

    def _search_node(self, node, key, count):
        # Busca um nó pela chave, retornando o nó encontrado e o número de comparações
        while node:
            count += 1
            if key == node.key:
                return node, count
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None, count  # Retorna None se não encontrado
