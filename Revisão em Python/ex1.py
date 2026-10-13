# ex 1

print("")
salario = float(input("Digite seu salário por hora: "))
horas = float(input("Digite o numero de horas trabalhadas no dia: "))

horasm      =   horas             * 30
salariob    =   (horasm           * salario)
ir          =   (salariob/100)    * 11
inss        =   (salariob/100)    * 8
sindicato   =   (salariob/100)    * 5
salariol    =   salariob - ir - inss - sindicato

print(f"\nSalário bruto: {salariob} R$ \nDesconto do Imposto de Renda: {ir} R$ \nDesconto do INSS: {inss} R$ \nDesconto do sindicato: {sindicato} R$ \nSalário liquido: {salariol} R$\n")