'''
Escreva um programa em Python que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
Telefonou para a vítima?
Esteve no local do crime?
Mora perto da vítima?
Devia para a vítima?
Já trabalhou com a vítima?

O programa deve ter três funções:
Uma função que recebe como parâmetro a pergunta e retorna a resposta do usuário (0 para não ou 1 para sim);
Uma função que recebe uma lista com as respostas retorna a quantidade de respostas positivas (função quantidade_sim);
Uma função que recebe a quantidade de respostas positivas e retorna sua classificação: se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como "Suspeita“; entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".

'''

# 1510206 - Victor Hugo da Silva

lista = ("Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?")
respostas = []

def pergunta(lista):
    for i in range(len(lista)):
        print(lista[i])
        resposta = int(input("0 para não e 1 para sim: "))
        respostas.append(resposta)

def quantidade_sim(respostas):
    qtd = 0
    for i in range(len(respostas)):
        if(respostas[i] == 1):
            qtd+=1
    return qtd

def classificacao(qtd):
    classificacao = ""
    if(qtd == 0 or qtd == 1):
        classificacao = "Inocente"
    elif(qtd == 2):
        classificacao = "Suspeita"
    elif(qtd > 2 and qtd <= 4):
        classificacao = "Cúmplice"
    elif(qtd == 5):
        classificacao = "Assassino"
    return classificacao

pergunta(lista)
print(quantidade_sim(respostas))
print(classificacao(quantidade_sim(respostas)))
