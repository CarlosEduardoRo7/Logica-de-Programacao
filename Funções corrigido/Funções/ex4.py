# Elabore um script em linguagem Python com uma função que recebe como entrada um
# número inteiro positivo e retorne a soma de todos os inteiros positivos menores ou iguais a
# n.

def soma_inteiros(n):
    soma = sum(range(1, n + 1))
    return soma

n = 10

print(soma_inteiros(n))