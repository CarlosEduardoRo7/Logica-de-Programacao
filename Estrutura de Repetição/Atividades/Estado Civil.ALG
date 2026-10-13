Algoritmo "Estado Civil"

Var

nome : caracter
sigla : caracter

Inicio

escreva("Escreva seu nome: ")
leia(nome)

escreva("Escreva seu estado civil: ")
leia(sigla)

se (sigla = "S") entao
   escreval(" ")
   escreva("o estado civil de ", nome," é Solteiro")
   escreval(" ")
   
   senao
        se (sigla = "C") entao
        escreval(" ")
        escreva("o estado civil de ", nome," é Casado")
        escreval(" ")
        
        senao
             se (sigla = "V") entao
             escreval(" ")
             escreva("o estado civil de ", nome," é Viúvo")
             escreval(" ")
             
             senao
                  se (sigla = "D") entao
                  escreval(" ")
                  escreva("o estado civil de ", nome," é Divorciado")
                  escreval(" ")
                  
fimse
fimse
fimse
fimse

Fimalgoritmo