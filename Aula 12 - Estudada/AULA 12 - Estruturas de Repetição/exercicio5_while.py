lista = []
x = 0

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    x += n
    if n < 0:
        break

print(x+1)
