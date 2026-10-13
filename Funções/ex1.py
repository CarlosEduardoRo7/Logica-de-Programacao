# Utilize um script em linguagem Python com uma função que receba três notas de um
# aluno e que retorne a média dessas 3 notas.

def nota(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

nome = str(input("Digite o nome do aluno: "))
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
media = nota(n1, n2, n3)

print(f"A média de {nome} é: {media:.2f}")