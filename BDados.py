# Criei um dicionário de dicionários porque permite acessar ou
# atualizar qualquer produto diretamente pelo seu nome de forma
# direta (O(1)), sem a necessidade de percorrer uma lista.

estoque = {
    "Notebook": {"quantidade": 10, "preco": 3500.00},
    "Mouse Wireless": {"quantidade": 50, "preco": 89.90},
    "Teclado Mecânico": {"quantidade": 25, "preco": 249.90},
}

# Criei uma lista de dicionários porque facilita a iteração
# sequencial de todos os itens, a ordenação do estoque e segue
# o padrão estrutural amplamente utilizado em APIs (JSON).

estoque = [
    {"nome": "Notebook", "quantidade": 10, "preco": 3500.00},
    {"nome": "Mouse Wireless", "quantidade": 50, "preco": 89.90},
    {"nome": "Teclado Mecânico", "quantidade": 25, "preco": 249.90},
]
