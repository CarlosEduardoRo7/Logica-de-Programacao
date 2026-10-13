# ex2 - forma correta de se fazer
# nota = a outra está certa, mas isso que o enunciado pede

print("")
C  = float(input("Digite a temperatura em Celsius: "))

F  = C * 1.8 + 32
K  = C + 273.15
RE = C * 0.8

e = int(input('''
                      
Qual temperatura você deseja converter?
              
1 - Fahrenheit
2 - Kelvin
3 - Réaumur       

'''))

print("")

if e == 1:
    print(f"Sua temperatura é: {F:.2f}")
elif e == 2:
    print(f"Sua temperatura é: {K:.2f}")
elif e == 3:
    print(f"Sua temperatura é: {RE:.2f}")
else:
    print("Valor inválido")