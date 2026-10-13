# Utilize um script em linguagem Python com uma função que receba três notas de um
# aluno e que retorne a média dessas 3 notas.

def nota(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    return media

n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
media = nota(n1, n2, n3)

print(f"A média é: {media:.2f}")