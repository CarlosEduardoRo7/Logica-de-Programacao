dicionario = {}

dicionario["nome"] = input("Digite o nome do aluno: ")

print("")
m = float(input("Digite a média do aluno: "))

if m >= 7:
    dicionario["situação"] = "Aprovado"
else:
    dicionario["situação"] = "Reprovado"

print("")
print(f"{dicionario["nome"]} foi {dicionario["situação"]}")

print("")