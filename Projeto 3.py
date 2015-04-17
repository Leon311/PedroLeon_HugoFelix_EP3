# -*- coding: utf-8 -*-

alimentos = open ("alimentos.csv", "r")
usuario = open ("usuario.csv", "r")

def harris_benedict(sexo, peso, altura, idade):
    if sexo =="h" or sexo =="H":
        tmb=0    
        tmb=66+(13.7+peso(kg))+(5*a(cm))-(6.8*idade) 
    elif sexo=="m" or sexo=="M":
        tmb=655+(9.6*peso(kg))+(1.8*a(cm))-(4.7*idade)
    
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
    return caloria
    
def imc(a,peso):
    imc=peso/a*a
    return imc
    

lista=list()
for i in alimentos: 
    lista2=(i.strip())
    lista.append(lista2.split(","))
    
    
    
#print(lista)    
    


dicionariocomida=dict()
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j==0:
            dicionariocomida[lista[i][j]]=list()
        else:
            dicionariocomida[lista[i][0]].append(lista[i][j])
#print(dicionariocomida)
        

"""       
if j==0:
    dicionariousuario[lista[i][j]]=list()
else:
    dicionariousuario[lista[i][0]].append(lista[i][j])
"""            

lista=list()
for i in usuario: 
    lista2=(i.strip())
    lista.append(lista2.split(","))
print(lista)
    
dicionariousuario=dict()
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j] in dicionariousuario:
            print(dicionariousuario)



datas = []
alimentos = []
for key, values in dicionariousuario.items():
    a = key
    datas.append(a)
    b = values
    alimentos.append(b)
print (a)
print (b)

listacaloria=list()
listaproteina=list()
listacarboidrato=list()
listagordura=list()
#j é os alimenots e j+1 é as qtd 
#j é a posiçaõ da lista do dicionário i
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
            


          