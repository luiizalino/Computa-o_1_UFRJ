
#Maria Luiza Lino de Souza
#DRE: 119162682


#Questão1

import math

def soma(n):
"""
int->float
:param n: Recebe um numero n.
:param return: Retorna o somatorio dos n termos.
"""
    soma=0
    for el in range(n+1):
        multiplicador=(-1)**el
        denominador=2*el+1
        soma += (1/denominador * multiplicador)
    return soma

def CalculaErro():
"""
float->tupla
:param return: Com base no soma, calcula o erro e retorna a tupla.
"""
    n=0
    valor=1
    while math.fabs(soma(n) - math.pi/4) >= 0.01:
        n+=1
        valor=soma(n)
    return (valor,n)
    
    

#Questão2

def criaContato(nome,telefone="",email="",instagram=""):
"""
str,str->lista
:param nome: Recebe o nome da pessoa dentro de uma lista de contatos
:param telefone: Recebe uma lista com informações sobre o contato
:param return: Retorna a lista do contato que a pessoa está buscando.
"""
    novoContato=[nome,[telefone],email,instagram]
    return novoContato

def atualizaContato(lista,indice,novaInfo):
    if indice  == 0 or indice == 2 or indice == 3:
        lista[indice]= novaInfo
        return True
    elif indice == 1:
        for el in lista[1]:
            if novaInfo == el:
                lista[1].remove(novaInfo)
                return True
        lista[1].append(novaInfo)
        return True
    else:
        return False
    
 def  buscaContato(listaContatos,nome):
    lista=[]
    for el in listaContatos:
        if nome in el:
            lista.append(el)
    return lista       
        
            
            
