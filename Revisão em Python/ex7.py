nome    =   input("Digite seu nome: ")
peso    =   float(input("Digite seu peso: "))
altura  =   float(input("Digite sua altura: "))

IMC = (peso / (altura*altura))

if IMC < 18.5:
    print(f"{nome}, você é abaixo do peso")

elif (IMC >= 18.5) and (IMC <= 25):
    print(f"{nome}, você tem peso normal")

elif (IMC > 25) and (IMC <= 30):
    print(f"{nome}, você é acima do peso")

elif (IMC > 30 ):
    print(f"{nome}, você é acima do obeso")