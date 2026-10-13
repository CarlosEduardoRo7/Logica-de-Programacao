Algoritmo "Aposentadoria"

Var

nome : caracter
g : caracter
idade : inteiro
contribuicao : inteiro

Inicio

escreva("Escreva seu nome: ")
leia(nome)

escreva("Digite sua idade: ")
leia(idade)

escreva("Digite seu tempo de contribuição: ")
leia(contribuicao)

escreva("Qual seu gênero: ")
leia(g)

escreval("")

se (g = "masculino") entao

   se (idade >= 65) e (contribuicao >= 30) entao
      escreva(nome ,", você pode se aposentar")
      escreval("")
   
      senao
           escreva(nome,", você não pode se aposentar")
           escreval("")
           
      fimse
      
senao

se (g = "feminino") entao

   se (idade >= 60) e (contribuicao >= 25) entao
      escreva(nome ,", você pode se aposentar")
      escreval("")

      senao
           escreva(nome,", você não pode se aposentar")
           escreval("")
         
      fimse

fimse
fimse
     
Fimalgoritmo