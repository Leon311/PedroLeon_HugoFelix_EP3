# -*- coding: utf-8 -*-

limentos = open ("alimentos.csv", "r")
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








     