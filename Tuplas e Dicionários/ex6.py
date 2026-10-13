produtos = {
    "Caneta": (2.50, 10),
    "Caderno": (15.00, 5),
    "Borracha": (1.00, 20)
}

print("")
for produto, valores in produtos.items():
    print(f"o estoque total do produto: {produto} é {valores[0]*valores[1]} R$")

print("")