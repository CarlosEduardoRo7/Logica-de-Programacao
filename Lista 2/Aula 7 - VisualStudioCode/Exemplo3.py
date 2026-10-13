# faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print("")
nome = input("Escreva seu nome: ")
valor = float(input("Escreva o preço de seu produto: "))
print("")

desconto = valor/100
novovalor = valor - desconto*5
print("")

print(f"{nome}, você ganhou 5% de desconto! seu novo valor é R$ {novovalor}")
print("")