'''
Um hospital precisa de um programa para calcular e imprimir os gastos de um
paciente. A tabela de preços do hospital a seguinte:

Quartos (diária):
Particular: R$ 160,00
Semi-particular: R$ 110,00
Coletivo: R$ 85,00

Telefone (uso): R$ 3,00
Televisão (uso): R$ 4,00

Escreva um programa em Python que leia: o número de dias gastos no hospital; um
caractere representando o tipo do quarto (P, S, C); um caractere indicando se usou ou
não o telefone (S, N); outro caractere indicando se usou ou não a televisão (S, N).
Então emita o seguinte relatório:

Hospital Comunitário
Número de dias no hospital: 6
Tipo de quarto: P
Diárias.............960.0
Telefone............0.0
Televisão...........0.0
Total...............960.0

'''
dias = int(input(""))
quarto = input("")
tel = input("")
tv = input("")

if(quarto == "P"):
  diarias = 160.0*dias
elif(quarto == "S"):
  diarias = 110.0*dias
elif(quarto == "C"):
  diarias = 85.0*dias
else:
  print("Opção inválida!")

if(tel == "S"): 
  tel = 3.0
elif(tel == "N"):
  tel = 0.0
else:
  print("Opção inválida!")
  
  
if(tv == "S"): 
  tv = 4.0
elif(tv == "N"):
  tv = 0.0
else:
  print("Opção inválida!")

print("Hospital Comunitário")
print("Número de dias no hospital:", dias)
print("Tipo de quarto:", quarto)
print("Diárias............." + str(diarias))
print("Telefone............" + str(tel))
print("Televisão..........." + str(tv))
print("Total..............." + str(diarias+tel+tv))