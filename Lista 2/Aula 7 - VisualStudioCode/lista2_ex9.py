print("")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("")
operacao = str(input("Qual operação você deseja realizar? ")).lower()

if operacao == "soma":
    print(n1 + n2)

elif operacao == "divisão":
    print(n1/n2)

elif operacao == "multiplicação":
    print(n1*n2)

elif operacao == "potenciação":
    print(n1**n2)