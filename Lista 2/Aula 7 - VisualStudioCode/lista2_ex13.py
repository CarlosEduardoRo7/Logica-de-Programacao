print("")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

A1 = n1+n2
media = (A1+n3)/2

if media >= 6:
    print(f"O aluno foi aprovado com a média de {media} pontos")

else:
    if media < 6:
       print(f"O aluno foi reprovado com a média de {media} pontos")