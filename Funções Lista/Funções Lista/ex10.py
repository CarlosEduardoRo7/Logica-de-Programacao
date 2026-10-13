import random

print(f"\nNúmero aleatório: {random.randint(1, 100)}")

nomes = ["Carlos", "Bia", "Ana"]
numeros = [1, 2, 3, 4, 5]

print(f"\nNome aleatório: {random.choice(nomes)}")
random.shuffle(numeros)
print(f"\nNome aleatório: {numeros}")