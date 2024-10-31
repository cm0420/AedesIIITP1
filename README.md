# Estruturas de Dados para Busca #
Este projeto realiza a comparação de desempenho entre diferentes estruturas de dados (Lista Sequencial, Árvore Binária e Árvore AVL) para operações de busca. São realizados testes de busca em conjuntos de dados de tamanhos variados, com dados organizados de forma ordenada e aleatória. Os resultados incluem o número de comparações e o tempo de execução para cada estrutura e tipo de dado, armazenados em um relatório final.

# Estrutura do Projeto #
O projeto está organizado da seguinte forma:

project/
├── printipal.py                # Script principal para executar o projeto
├── tree/                   # Estruturas de dados para armazenar e buscar registros
│   ├── sequential.py       # Implementação da lista sequencial
│   ├── Bn_Tree.py          # Implementação da árvore binária
│   └── AvL_tree.py         # Implementação da árvore AVL
├── Random_Functions/       # Funções para geração de dados e seleção de chaves
│   ├── random_know_key.py  # Função para selecionar chaves conhecidas
│   ├── random_unknow_key.py# Função para gerar chaves desconhecidas
│   └── random_data_file.py # Função para gerar dados aleatórios em arquivos CSV
├── functions/              # Funções utilitárias para carregar e salvar dados
│   ├── Ld_csv.py           # Função para carregar registros a partir de arquivos CSV
│   └── sv_rprt.py          # Função para salvar o relatório de busca
├── data/                   # Pasta para armazenamento dos arquivos de dados gerados
└── reports/                # Pasta onde o relatório final de busca é salvo

Requisitos
Para executar este projeto, você precisa ter o Python (3.6 ou superior) instalado em sua máquina.

# Instalação #
Clone este repositório em sua máquina:


git clone <URL do repositório>
cd project


Certifique-se de que você está no diretório raiz do projeto.

# Executando o Projeto #
Execute o script principal:


python index.py


Ao rodar o script, o projeto irá:

Gerar arquivos CSV com tamanhos de dados variados (100, 500, 1000, 5000 e 10000 registros).
Preencher as estruturas de dados (Lista Sequencial, Árvore Binária e Árvore AVL) com os dados gerados (aleatórios e ordenados).
Realizar buscas com chaves conhecidas e desconhecidas para cada estrutura.
Salvar o relatório final no diretório reports no formato search_report.csv.

