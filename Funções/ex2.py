# Agora, faça uma função de acordo com a média da função anterior e informe o status do
# aluno de acordo com a tabela a seguir:

def nota(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def desempenho(media):
    if media > 6:
        print(f"{nome} foi APROVADO")
    elif (media >= 4) and (media <= 6):
        print(f"{nome} foi VERIFICAÇÃO SUPLEMENTAR")
    elif media < 4:
        print(f"{nome} foi REPROVADO")

nome = str(input("Digite o nome do aluno: "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = nota(n1, n2, n3)

print(f"A média de {nome} é: {media:.2f}")
desempenho(media)