import math

recomecar = 0

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2


while True:
    print('''       
1 - Calcular adição
2 - Calcular subtração
3 - Calcular multiplicação
4 - Calcular divisão
5 - Calcular potenciação
6 - Sair
''')
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"\nA soma dos números {n1} e {n2} é: {adicao(n1,n2)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    if escolha == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"\nA subtração dos números {n1} e {n2} é: {subtracao(n1,n2)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    if escolha == 3:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"\nA multiplicação dos números {n1} e {n2} é: {multiplicacao(n1,n2)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    if escolha == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"\nA divisão dos números {n1} e {n2} é: {divisao(n1,n2)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    if escolha == 5:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f"\nA potencia dos números {n1} e {n2} é: {pow(n1,n2)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    if escolha == 6:
        break