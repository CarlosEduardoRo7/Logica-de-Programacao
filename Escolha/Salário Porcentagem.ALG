Algoritmo "Salário Porcentagem"

Var

nome : caracter
salario : real

Inicio

escreva("Escreva seu nome: ")
leia(nome)
escreval("")

escreva("Digite seu salário final: ")
leia(salario)
escreval("")

escolha(salario)

caso 1000 ate 1500

escreva("Você receberá: ", (10*salario)/100 ,"R$ de aumento")
escreval("")

caso 1501 ate 1999

escreva("Você receberá: ", (8*salario)/100 ,"R$ de aumento")
escreval("")

caso >= 2000

escreva("Você receberá: ", (5*salario)/100 ,"R$ de aumento")
escreval("")

fimescolha

Fimalgoritmo