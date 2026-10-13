Algoritmo "semnome"

Var

nome : caracter
idade : inteiro
peso: real

Inicio

escreva("Escreva seu nome: ")
leia(nome)

escreval("")

escreva("Digite sua idade: ")
leia(idade)

escreval("")

escreva("Digite seu peso: ")
leia(peso)

escreval("")

se (idade >= 0) e (idade <= 15) entao
   escreva(nome ," você não pode ser doador de sangue")
   
   senao
   
   se (idade >= 16) e (idade <= 17) entao

      se (peso >= 50) entao
      
         escreva(nome ,", você pode ser doador de sangue com autorização de seus responsáveis")
         escreval("")
         
      senao

           se (idade >= 18) e (idade <= 69) entao
           
           escreva(nome ,", você pode ser doador de sangue")
           escreval("")
           
           senao
           
           escreva(nome ,", você não pode ser doador de sangue")
           escreval("")
           
           fimse
           
     fimse
     
   fimse
   
fimse

Fimalgoritmo