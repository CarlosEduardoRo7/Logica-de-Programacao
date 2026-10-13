# Para construir o programa a seguir, considere que os usuários só informarão
# números inteiros positivos. Crie um programa que receba 10 números digitados e
# exiba a média dos números lidos.

i = 0
med = 0

while i < 10:
    n = int(input("Digite seu numero: "))
    i += 1
    med += n

print(med/10)