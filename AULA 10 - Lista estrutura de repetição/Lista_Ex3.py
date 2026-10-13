print('')

coisas = []
soma = 0
itens = 0

for valor in range(5):

    valor = int(input('Digite o valor: '))
    coisas.append(valor)
    soma = soma + valor

    print('')
    print(f'O valor é: {valor:.0f}')
    print('')

print(f'A soma final é: {soma:.0f}')
print('')