Algoritmo "Nome e Idade"

Var

nome : caracter
idade : inteiro

Inicio

escreva("Digite seu nome: ")
leia(nome)

escreva("Digite sua idade: ")
leia(idade)

se ( idade >= 0) e (idade <= 12) entao
escreval(" ")
escreva("Olá ", nome , "! Você é uma criança de", idade , " anos!")
escreval(" ")

             senão
             se ( idade >= 13 ) e ( idade <= 17 ) entao
             escreval(" ")
             escreva("Olá ", nome , "! Você é um adolescente de", idade , " anos!")
             escreval(" ")
             
                        senão
                        se ( idade >= 18 ) e ( idade <= 59 ) entao
                        escreval(" ")
                        escreva("Olá ", nome , "! Você é um adulto de", idade , " anos!") entao
                        escreval(" ")
                        
                                   senão
                                   se ( idade >= 60 ) entao
                                   escreval(" ")
                                   escreva("Olá ", nome , "! Você é um idoso de", idade , " anos!")
                                   escreval(" ")


fimse
fimse
fimse
fimse

Fimalgoritmo