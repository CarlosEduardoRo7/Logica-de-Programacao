# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa
# Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros

print("")
reais = float(input("Digite quantos reais você possui: "))
valor = 5.41
valoreuro = 6.19
print("")


dolar = reais/valor
euros = reais/valoreuro

print(f"Você possui R$ {reais}, você consegue comprar US$ {dolar:.2f} ou {euros:.2f} €!")
print("")