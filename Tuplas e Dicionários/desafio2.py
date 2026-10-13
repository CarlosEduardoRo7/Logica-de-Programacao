dados = {
    "Carlos": [7, 8, 9],
    "Felipe": [6, 5, 7]
}

for alunos, notas in dados.items():
    med = (notas[0]+notas[1]+notas[2])/3
    
    print("")
    if med >= 7:
        print(f"{alunos} foi aprovado com a média de: {med} pontos")