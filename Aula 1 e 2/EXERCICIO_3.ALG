Algoritmo "semnome"

Var

nota1, nota2, nota3, MEDIA : real


Inicio

ESCREVA("Escreva sua Nota 1: ")
LEIA(nota1)

ESCREVA("Escreva sua Nota 2: ")
LEIA(nota2)

ESCREVA("Escreva sua Nota 3: ")
LEIA(nota3)

	MEDIA <- (nota1 + nota2 + nota3) /3
	escreval(" ")
	Se media < 7 Então
		Escreva ("Reprovado: " , MEDIA)
	Senão
		Escreva ("aprovado: " , MEDIA)
		escreval(" ")
	fimse

Fimalgoritmo