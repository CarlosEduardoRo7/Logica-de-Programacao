print("")
print("EXEMPLO 3")
nomes = []

print("")
while True:
    nome = input("Digite seu nome (ou sair para parar): ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)

print("")

for i in nomes:
    print(i)

print("")