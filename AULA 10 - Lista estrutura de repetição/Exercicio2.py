print('')

coisas = []
soma = 0
itens = 0

for valor in range(5):

    valor = float(input('Digite o valor: '))
    coisas.append(valor)
    soma = soma + valor
    itens = itens + 1

    print('')
    print(f'O valor é: {valor:.0f}')
    print(f'A soma é: {soma:.0f}')
    print('')

print(f'A soma final é: {soma:.0f}')
print('')

print(coisas)
print('')

print(f'Existem {itens} itens nessa lista')
print('')