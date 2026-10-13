Algoritmo "Nota Aluno"

Var

Nome : caractere
Idade : real

Inicio

      escreva("Escreva o seu nome: ")
      leia(Nome)

      escreval("")

      escreva("Digite a sua idade: ")
      leia(Idade)

      escreval("")

escolha(Idade)

      caso 0 ate 12
      escreva(Nome ,", Você é criança.")
      escreval("")
                  
      caso 13 ate 17
      escreva(Nome ,", você é adolescente.")
      escreval("")
      
      caso 18 ate 59
      escreva(Nome ,", você é adulto.")
      escreval("")
      
      caso 59 ate 123
      escreva(Nome ,", você é idoso.")
      escreval("")
      
      outrocaso
      escreva(Nome ,", você é um fantasma, ou imortal.")
      escreval("")
                  
fimescolha

Fimalgoritmo