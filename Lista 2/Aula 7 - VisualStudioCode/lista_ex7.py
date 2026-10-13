# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.

print("")
nome = input("Escreva seu nome: ")
valor = float(input("Escreva o preço de seu produto: "))
print("")

desconto = valor/100
novovalor = valor - desconto*5
nvm = valor + desconto*15
print("")

print(f"{nome}, em caso de desconto, o produto ficará R$ {novovalor}")
print("")

print(f"{nome}, em caso de aumento, o produto ficará R$ {nvm}")
print("")