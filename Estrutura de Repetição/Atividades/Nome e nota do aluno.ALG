Algoritmo "Nome e nota Aluno"

Var

nome : caracter
nota1 : real
nota2 : real
nota3 : real
media : real
Inicio

escreva("Digite o nome do aluno: ")
leia(nome)
escreval(" ")

escreva("Digite a primeira nota do aluno ")
leia(nota1)
escreval(" ")

escreva("Digite a segunda nota do aluno ")
leia(nota2)
escreval(" ")

escreva("Digite a terceira nota do aluno ")
leia(nota3)
escreval(" ")

media <- (nota1+nota2+nota3) /3

se (media < 5) entao
   escreval(" ")
   escreva(media)
   
   senao
        se (media >= 5) e (media < 7) entao
        escreva(media)
           
           senao
                      
                      se (media >= 7) entao
                      escreval(" ")
                      escreva(media)
   fimse
   fimse
   fimse
   Fimalgoritmo