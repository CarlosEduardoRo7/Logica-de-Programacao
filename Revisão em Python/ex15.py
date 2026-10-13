lista = []

while True:

    print('''

--- Tabela de Opções ---

1 - Adcionar um número
2 - Remover um número
3 - Exibir todos os números
4 - Exibir somene números pares
5 - Exibir somente números impares
6 - Exibir somente números primos

''')

    op = int(input("Digite o número de sua opção: "))

    if op == 1:
        add = int(input("Digite o número que você deseja adcionar: "))
        lista.append(add)

    elif op == 2:
        rem = int(input("Digite o número que você deseja remover: "))
        lista.remove(rem)
    
    elif op == 3:
        print(lista)
    
    elif op == 4:
        print("Números pares:")
        print("")
        for i in range(len(lista)):
            if lista[i]%2 == 0:
                print(f"{lista[i]}")

    elif op == 5:
        print("Números impares:")
        print("")
        for i in range(len(lista)):
            if lista[i]%2 != 0:
                print(f"{lista[i]}")
    
    elif op == 6:
        print("Números primos:")
        print("")
        for i in range(len(lista)):
            if (lista[i]%2 != 0) and (lista[i]%3 != 0):
                print(f"{lista[i]}")