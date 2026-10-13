valor = int(input("Digite o seu valor: "))
divisao = 0

for i in range(1, valor + 1 ):
    if valor % i == 0:
        divisao += 1

print(divisao)

if divisao == 2:
    
    print("é primo")

else:
    print("Não é não")
