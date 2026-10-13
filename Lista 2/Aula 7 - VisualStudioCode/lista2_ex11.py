print("")

valor = float(input("Escreva o valor desejado: "))
converter = str(input("Você deseja converter esse valor para Celsius ou Fahrenheit? ")).lower()

f = (valor*9/5)
f2 = (f + 32)

c1 = (valor - 32)
c2 = (c1 * 5/9)

print("")

if converter == "fahrenheit":
    print(f"O Valor convertido é de {f2:.2f} Fahrenheit")
    print("")

elif converter == "celsius":
    print(f"O Valor convertido é de {c2:.2f} Celsius")
    print("")

else:
    print("O Valor é invalido")