produtos = [('Banana', 5), ('Maça', 7), ('Chocolate', 2)]
ordenado = sorted(produtos, key=lambda x: x[1], reverse=True)
print(ordenado)