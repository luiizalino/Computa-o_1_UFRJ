
#Maria Luiza Lino de Souza
#DRE: 119162682


#Questão 1

def pegaDados():
    """
    lista->lista
    :param return: Retorna uma lista com o resultado do operador
    """
    lista=[]
    n=0
    while n < 7:
        n=int(input('Digite o resultado do dado ou um um numero superior a 6 para encerrar a sequencia'))
        lista.append(n)
    return lista

def main():
    """
    :param return: O main ultiliza a função anterior para contar o numero de ocorrencia de series.
    """
    elemento=0
    jaAlterou=0
    ocorrencias=0
    for el in pegaDados():
        if el == elemento and jaAlterou == 0:
            ocorrencias+=1
            jaAlterou = 1            
        elif el != elemento:
            jaAlterou = 0
        elemento=el
    print(ocorrencias)
    return
            
main()



#Questão 2

def calcula1(a,b,c):
    """
    3 int-> int
    :param a: Um numero inteiro positivo 
    :param b: Um numero inteiro positivo
    :param c: Um numero inteiro positivo
    :param return: Retorna a area do trapezio a,b,c.
    """
    return(a+b)*c/2

def calcula2(a,b,c):
    """
    3 int-> int
    :param a: Um numero inteiro positivo 
    :param b: Um numero inteiro positivo
    :param c: Um numero inteiro positivo
    :param return: Retorna o quadrado de a,b,c
    """
    return (a*a,b*b,c*c)

def calcula3(a,b,c):
    """
    3 int-> int
    :param a: Um numero inteiro positivo 
    :param b: Um numero inteiro positivo
    :param c: Um numero inteiro positivo
    :param return: Retorna a media aritimetica de a,b,c
    """
    return (a*b*c/3)

def calcula4(a,b,c):
    """
    3 int-> int
    :param a: Um numero inteiro positivo 
    :param b: Um numero inteiro positivo
    :param c: Um numero inteiro positivo
    :param return: Retorna a soma dos inteiros de a (inclusive) ate b (inclusive) com uma
variacao igual a c.
    """
    soma=0
    numero=a
    while numero+c<=b:
        soma+=numero
        numero+=c
    return numero

def main():
    """
    int->int
    :param return: le um codigo i, em um intervalo de 1 a 4, e 3 valores a, b, c inteiros e positivos,
com a < b e retorna de acordo com o codigo escolhido
    """
    i=int(input('Digite o codigo de 1-4'))
    a=int(input('Digite o valor de a'))
    b=int(input('Digite o valor de b'))
    c=int(input('Digite o valor de c'))
    if i==1:
        print(calcula1(a,b,c),i,a,b,c)
    elif i==2:
        print(calcula2(a,b,c),i,a,b,c)
    elif i==3:
        print(calcula3(a,b,c),i,a,b,c)
    elif i==4:
        print(calcula4(a,b,c))
    return 


main()


#Questão 3

def f(matriz):
    """
    matriz->srt
    :param matriz: Recebe uma matriz de entrada e pesquisa apenas as pessoas do setor desejado
    :param return: Retorna outra matriz apenas com essas pessoas.
    """
    retorno=[]
    setor=input('Diga o setor')
    for el in matriz:
        if setor in el:
            retorno.append(el)
    if retorno==[]:
        return 'nenhum registro encontrado'
    return retorno

matriz=[]
n='s'
while n == 's':
    el=[]
    el.append(input('digite o nome'))
    el.append(input('digite o registro'))
    el.append(input('digite o setor'))
    el.append(input('digite o telefone'))
    n=input('deseja continuar s ou n')
    matriz.append(el)

print(f(matriz))






            
