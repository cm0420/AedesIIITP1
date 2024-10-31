

class BinaryTreeNode:
    def __init__(self, key, data1, data2):
        self.key = key
        self.data1 = data1
        self.data2 = data2
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data1, data2):
        new_node = BinaryTreeNode(key, data1, data2)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None  # Usa um nó pai para fazer a inserção após o loop
        is_left_child = False

        # Estrutura de loop enquanto atualiza pai e direção
        while current:
            parent = current
            if key < current.key:
                current = current.left
                is_left_child = True
            elif key > current.key:
                current = current.right
                is_left_child = False
            else:
                # Tratamento de duplicatas: substituímos os dados do nó atual
                current.data1 = data1
                current.data2 = data2
                return

        # Após o loop, adiciona o novo nó como filho esquerdo ou direito do pai
        if is_left_child:
            parent.left = new_node
        else:
            parent.right = new_node

    def search_with_count(self, key):
        comparisons = 0
        current = self.root

        # Estrutura de loop para busca
        while current:
            comparisons += 1
            if key == current.key:
                return current, comparisons
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None, comparisons



