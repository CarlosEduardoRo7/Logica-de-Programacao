import time

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
        area_circulo = lambda r: 3.14*(r*r)

        print(f"\nA área do circulo é aproximadamente: {area_circulo(raio)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 2:
        base = float(input("Base do retangulo: "))
        altura = float(input("Altura do retangulo: "))
        area_retangulo = lambda b, h: b*h

        print(f"\nA área do circulo é aproximadamente: {area_retangulo(base, altura)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 3:
        base = float(input("Base do retangulo: "))
        altura = float(input("Altura do retangulo: "))
        area_triangulo = lambda b, h: (b*h)/2

        print(f"\nA área do circulo é aproximadamente: {area_triangulo(base, altura)}")

        recomecar = input("\nDeseja reiniciar? (Y/N) ").upper()
        if recomecar == "N":
            break

    elif escolha == 4:
        break