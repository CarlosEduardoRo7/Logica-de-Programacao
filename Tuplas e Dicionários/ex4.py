alunos = {"Felipe": 7.8, "Joana": 8.6, "Jonas": 6.9}

for aluno, notas in alunos.items():
    if notas >= 7:
        print(f"{aluno}: {notas} - Aprovado")