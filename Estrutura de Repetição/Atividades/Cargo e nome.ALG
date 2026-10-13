Algoritmo "Cargo e nome"

Var
      cargo : caracter
      nome: caracter
Inicio

     escreva("Qual o seu nome?: ")
     leia(nome)
     escreva("Qual o seu Cargo?: ")
     leia(cargo)
     escreval(" ")

     se ( cargo = "Vendedor" ) entao
        escreva("Oi ", nome , " seu cargo é Vendedor")
        escreval(" ")
        
     senao
          se ( cargo = "Contador") entao
          escreva("Oi ", nome , " seu cargo é Contador")
          escreval(" ")
          
          senao
               se ( cargo = "Técnico") entao
               escreva("Oi ", nome , " seu cargo é Técnico")
               escreval(" ")
               
               senao
               escreva("Oi ", nome , " você não trabalha em nenhum dos cargos")
               escreval(" ")
               escreva("Oi ", nome , " seu cargo é: " , cargo)
               escreval(" ")
               
               fimse
        
     fimse
     fimse

Fimalgoritmo