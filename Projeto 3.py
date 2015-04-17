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
print(dicionariocomida)
        


lista=list()
for i in usuario: 
    lista2=(i.strip())
    lista.append(lista2.split(","))
#print(lista)
    
dicionariousuario=dict()
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j] in dicionariousuario:
            
'''        
if j==0:
    dicionariousuario[lista[i][j]]=list()
else:
    dicionariousuario[lista[i][0]].append(lista[i][j])"""
'''            




print(dicionariousuario)
datas = []
alimentos = []
for key, values in dicionariousuario.items():
    a = key
    datas.append(a)
    b = values
    alimentos.append(b)
#print (datas)
#print (alimentos)
    



    