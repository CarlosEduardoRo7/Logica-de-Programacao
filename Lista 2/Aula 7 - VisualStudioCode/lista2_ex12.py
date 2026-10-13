h = float(input("Escreva sua altura em Metros: "))
g = str(input("Qual o seu Gênero: ")).lower()

h1 = (72.7 * h)
h2 = h1 - 58

f1 = (62.1 * h)
f2 = f1 - 44.7

if g == "masculino":
    print("")
    print(f"Seu peso ideal é: {h2:.2f}")

elif g == "feminino":
    print("")
    print(f"Seu peso ideal é: {f2:.2f}")