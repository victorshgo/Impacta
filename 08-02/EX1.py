'''
Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando
o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos
da tabela seguinte para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.

Código		Condições de pagamento
1		10% de desconto
2		5% de desconto
3		Sem juros
4		10% de juros

'''
preco = float(input("Digite o preço: "))
codigo = int(input("Digite o código de pagamento: "))

if(codigo == 1):
  preco -= preco/100*10
elif(codigo == 2):
  preco -= preco/100*5
elif(codigo == 3):
  preco = preco
elif(codigo == 4):
  preco += preco/100*10
else:
  print("\nForma de pagamento inválida")
  exit()
  
print("\nR$", preco)