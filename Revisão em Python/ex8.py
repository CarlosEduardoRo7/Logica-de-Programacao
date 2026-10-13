print("")
votantes = int(input("Numero de votantes: "))
votos1 = []
votos2 = []
votos3 = []

print("")

for i in range(votantes):

    v = int(input("Digite seu voto: "))

    if v == 1:
        votos1.append(v)
    elif v == 2:
        votos2.append(v)
    elif v == 3:
        votos3.append(v)
    else:
        print("")
        print("Voto inválido")
        print("")

print(f'''

Candidato 1 - {len(votos1)}
Candidato 2 - {len(votos2)}
Candidato 3 - {len(votos3)}

''')