'''
Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.

Por exemplo: 

Entrada: número 2, 3 e subtração (-)

Saída:
-1.0 é impar
-1.0 é negativo
-1.0 é inteiro

'''
n1 = float(input(""))
n2 = float(input(""))
operacao = input("")

if(operacao == "+"):  
	result = n1+n2
elif(operacao == "-"):
	result = n1-n2
elif(operacao == "*"):
	result = n1*n2
elif(operacao == "/"):
	result = n1/n2
else:
	print("Opção inválida!")



if(int(result)%2 == 0):
	print(result, "é par.")
else: 
	print(result, "é impar.")

if(result<0):
	print(result, "é negativo.")
else:
	print(result, "é positivo.")

if(result == int(result)):
	print(result, "é inteiro.")
else:  
	print(result, "é decimal.")
  