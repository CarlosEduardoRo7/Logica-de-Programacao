# Escreva um programa que lido um número, calcule e informe o seu fatorial.
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.

numero = int(input("Digite o número para descobrir o Fatorial: "))
antecessor = numero

while antecessor > 1:
    numero *=(antecessor-1)
    antecessor += -1

print(numero)