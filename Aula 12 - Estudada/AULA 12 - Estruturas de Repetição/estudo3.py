# escrever um programa que leia 10 número inteiros e, ao final, apresente a soma de todos os números lidos

soma = 0

for i in range(10):
    n = int(input("Digite um numero: "))
    soma += n

print(f"A soma dos numeros é: {soma}")