# escrever um programa que leia 10 número inteiros e, ao final, apresente a soma de todos os números lidos

lista = []
soma = 0
x = 0

while x < 10:

    n = int(input("Digite o número: "))
    lista.append(n)
    print("")
    soma += n
    x += 1

print(lista)
print("")

print(f"A soma é: {soma}")
print("")