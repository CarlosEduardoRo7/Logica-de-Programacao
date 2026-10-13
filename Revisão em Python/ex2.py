# ex2

print("")
C  = float(input("Digite a temperatura em Celsius: "))

F  = C * 1.8 + 32
K  = C + 273.15
RE = C * 0.8

print(f''' 
1 - Graus Fahrenheit    =       {F}
2 - Graus Kelvin        =       {K}
3 - Graus Réaumur       =       {RE:.2f}
''')
