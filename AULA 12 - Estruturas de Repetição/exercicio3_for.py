# escrever um programa que leia 10 valores inteiros e encontre o maior e o menor deles.

lista = []
print("")

for i in range(10):

    n = int(input("Digite o número: "))
    lista.append(n)
    print("")

print(f"Seu valor máximo é: {max(lista)}")

print("")
print(f"Seu valor mínimo é: {min(lista)}")