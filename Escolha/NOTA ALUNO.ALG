Algoritmo "Nota Aluno"

Var

Nome : caractere
Nota : real

Inicio

      escreva("Escreva o nome do Aluno: ")
      leia(Nome)

      escreval("")

      escreva("Digite a Nota final do Aluno: ")
      leia(Nota)

      escreval("")

escolha(Nota)

      caso 0 ate 4
      escreva(Nome ,", infelizmente, você foi REPROVADO.")
      escreval("")
                  
      caso 5 ate 6
      escreva(Nome ,", você ficou em RECUPERAÇÃO.")
      escreval("")
                  
      outrocaso
      escreva(Nome ,", você foi APROVADO")
      escreval("")

fimescolha

Fimalgoritmo