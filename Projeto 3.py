# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 

alimentos = open ("alimentos.csv", "r")
usuario = open ("usuario1.csv", "r")

def harris_benedict(sexo, peso, altura, idade):
    if sexo =="m" or sexo =="M":
        tmb=66+(13.7*float(peso))+(5*float(altura)*100)-(6.8*float(idade)) #peso en kg, altura em cm.
    elif sexo=="f" or sexo=="F":
        tmb=655+(9.6*float(peso))+(1.8*float(altura)*100)-(4.7*float(idade))
    
    return tmb
    
    
def caloria(tmb,fator):
    if fator== "mínimo":
        caloria_dia=tmb*1.2
    if fator== "baixo": 
        caloria_dia=tmb*1.375
    if fator=="medio":
        caloria_dia=tmb*1.55
    if fator=="alto":
        caloria_dia=tmb*1.725
    if fator=="muito alto":
        caloria_dia=tmb*1.9
    return caloria_dia
    
def imc(altura,peso):
    imc=int(peso)/float(altura)*float(altura)
    return imc
    
print("\nlimpa espaços da lista de alimentos\n")

lista=list()
for i in alimentos: 
    lista2=(i.strip())
    lista.append(lista2.split(","))
print(lista)    
    

print("\nMonta dicionário de alimentos\n")
dicionariocomida=dict()

for i in range(len(lista)):
    for j in range(len(lista[i])):       
        if j==0:
            dicionariocomida[lista[i][j]]=list()
        else:
            dicionariocomida[lista[i][0]].append(lista[i][j])
print(dicionariocomida)
        

print("\nlimpa espaços da lista de usuários\n")
listau=list()
for i in usuario: 
    lista2=(i.strip())
    listau.append(lista2.split(","))
print(listau)

print("\nOrdena lista de usuário por data\n")

fim=len(listau)
while fim>4:
    trocou=False
    x=3
    while x<(fim-1):
        
        if listau[x][0] > listau[x+1][0]:
            trocou=True
            print(trocou)
            temp=listau[x]
            listau[x]=listau[x+1]
            listau[x+1]=temp
        x+=1
        if not trocou:
            break
    fim-=1
for e in listau:
    print (e)
"""    
print("\nMonta dicionário de usuários\n")   
dicionariousuario=dict()
for i in range(1,len(listau)):
    for j in range(len(listau[i])):
        if j==0:
            dicionariousuario[listau[i][j]]=list()
        else:
            dicionariousuario[listau[i][0]].append(listau[i][j])     
print(dicionariousuario)
"""
print("\nCálculo da quantidade diária recomendada de calorías\n")


calorias6=0
calorias7=0

SEXO=listau[1][3]
PESO=listau[1][2]
ALTURA=listau[1][4]
IDADE=listau[1][1]
FATOR=listau[1][5]

print(listau[0])
print("Fulano da Silva:", IDADE,PESO,SEXO,ALTURA,FATOR)
TMB=harris_benedict(SEXO,PESO,ALTURA,IDADE)
print("tmb: %4.2f" % TMB)
caloriadia=caloria(TMB,FATOR)
print ("Caloria recomendada por dia: %4.2f" % caloriadia)
IMC=imc(ALTURA,PESO)
print("IMC: %4.2f\n"% IMC)

print("\nCálculo da quantidade diária de calorías consumida por Fulano da Silva\n")

dia6=[3,4,5,6]
dia7=[7,8,9,10]

for x in dia6:
    if listau[x][1] in dicionariocomida:
        quant, cal, prot, carb, gord=dicionariocomida[listau[x][1]]
        calorias6+=float((listau[x][2])) * float(cal)/int(quant)
        
    else:
        print("Alimento não encontrado no dicionario")
for x in dia7:
    if listau[x][1] in dicionariocomida:
        quant, cal, prot, carb, gord=dicionariocomida[listau[x][1]]
        calorias7+=float((listau[x][2])) * float(cal)/float(quant)
        
    else:
        print("Alimento não encontrado no dicionario")
print("Quantidade de calorias do dia 06/04/15:", calorias6)        
print("Quantidade de calorias do dia 07/04/15:", calorias7)   
print("\n\n")
    
datas = []
alimentos = []
dicionariousuario=dict()
"""for key, values in dicionariousuario.items():
    a = key
    datas.append(a)
    b = values
    alimentos.append(b)
print (a)
print (b)
"""
listacaloria=list()
listaproteina=list()
listacarboidrato=list()
listagordura=list()
#j é os alimenots e j+1 é as qtd 
#j é a posição da lista do dicionário i
#i é uma chave, alimento

#aqui quanto de caloria prot etc por dia
for i in dicionariousuario.keys():
    lista4bagos=[0]*4 #1=caloria 2=proteina 3=carboidrato 4=Gordura
           
    if i [2]=="/":
        for j in range(0,len(dicionariousuario[i]),2):
            proporcao=float(dicionariousuario[i][j+1])/float(dicionariocomida[dicionariousuario[i][j]][0])
            lista4bagos[0]+=float(dicionariocomida[dicionariousuario[i][j]][1])*proporcao #dic usuario pega alimento dentro do dic comida  
            lista4bagos[1]+=float(dicionariocomida[dicionariousuario[i][j]][2])*proporcao
            lista4bagos[2]+=float(dicionariocomida[dicionariousuario[i][j]][3])*proporcao
            lista4bagos[3]+=float(dicionariocomida[dicionariousuario[i][j]][4])*proporcao
        listacaloria.append(lista4bagos[0])
        listaproteina.append(lista4bagos[1])
        listacarboidrato.append(lista4bagos[2])
        listagordura.append(lista4bagos[3])    
pedro = list()
pedro.append(calorias6)
pedro.append(calorias7)
T = [1,2]


plt.plot(T,pedro)
plt.ylabel('Calorias')
plt.xlabel('Dias')
plt.title("Calorias diarias")
plt.show()

