from functools import reduce

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 4', 'preco': 105.87},
    {'nome': 'Produto 5', 'preco': 69.90}
]

def funcaoReduce(acumulator, produto):
    print('acumulator', acumulator)
    print('produto', produto)
    print()
    return acumulator + produto['preco']

total = reduce(
    funcaoReduce,
    produtos,
    0
)

""" total = 0
for produto in produtos:
    total += produto['preco']

print(total) """