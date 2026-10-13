alturalista = []
m = []
x = 0
h = 0
w = 0

for i in range(49):

    x += 1
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura: "))
    sexo = str(input("Digite o seu sexo: ").lower)

    alturalista.append(altura)

    if sexo == "mfeminino":
        m.append(altura)
        w += 1
    
    elif sexo == "masculino":
        h += 1
    print("")


print(f'''

Maior altura = {max(alturalista)}
Média da altura das mulheres = {(sum(m)/x):.2f}
Número de homens = {h}
porcentagem de homens = {(50*len(h)/100)}
porcentagem de mulheres = {(50*len(w)/100)}

''')