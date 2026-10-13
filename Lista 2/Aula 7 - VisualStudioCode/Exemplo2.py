# faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# considere US$ 1.00 = R$ 5.41

print("")
reais = float(input("Digite quantos reais você possui: "))
valor = 5.41
print("")


dolar = reais/valor
print(f"Você possui R$ {reais}, você consegue comprar US$ {dolar:.2f}!")
print("")