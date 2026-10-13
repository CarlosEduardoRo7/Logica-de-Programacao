print("")
nome = input("Digite seu nome ou (Sair): ")

while True:
    if nome == "sair":
        break
    else:
        print(f"Seu nome é: {nome}")
        nome = input("Digite seu nome ou (Sair): ")