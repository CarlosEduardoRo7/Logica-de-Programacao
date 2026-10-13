nome = str(input("Digite o seu nome: "))
idade = int(input("Digite sua idade: "))
vp = float(input("Digite o valor do seu plano: "))

if (idade > 0) and (idade <= 18):
    print(f"O novo valor do seu plano é: {((vp/100)*5) + vp} R$")

elif (idade > 19) and (idade <= 35):
    print(f"O novo valor do seu plano é: {((vp/100)*10) + vp} R$")

elif (idade > 36) and (idade <= 60):
    print(f"O novo valor do seu plano é: {((vp/100)*15) + vp} R$")

elif (idade > 60):
    print(f"O novo valor do seu plano é: {((vp/100)*20) + vp} R$")