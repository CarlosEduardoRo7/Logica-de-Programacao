# escrever um programa que leia 10 número inteiros e, ao final, apresente a soma de todos os números lidos

lista = []
soma = 0

for i in range(10):

    n = int(input("Digite o número: "))
    lista.append(n)
    print("")
    soma = soma + n

print(lista)

print("")
print(f"A soma é: {soma}")