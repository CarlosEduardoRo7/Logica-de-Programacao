import time

def area_do_circulo(r):
    return 3.14 * r**2

def area_do_retangulo(b, h):
    return b*h

def area_do_triangulo(b, h):
    return (b*h)/2

while True:
    print('''       
1 - Calcular a área de um circulo
2 - Calcular a área de um retangulo
3 - Calcular a área de um triângulo
4 - Sair

''')
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        raio = float(input("Raio do Circulo: "))

        print(f"\nA área do circulo é aproximadamente: {area_do_circulo(raio)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 2:
        base = float(input("Base do retangulo: "))
        altura = float(input("Altura do retangulo: "))

        print(f"\nA área do circulo é aproximadamente: {area_do_retangulo(base, altura)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 3:
        base = float(input("Base do retangulo: "))
        altura = float(input("Altura do retangulo: "))

        print(f"\nA área do circulo é aproximadamente: {area_do_triangulo(base, altura)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 4:
        break