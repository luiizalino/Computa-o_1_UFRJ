
#Maria Luiza Lino de Souza
#DRE: 119162682


#Questão 1


def multiplicacao(matriz,n):
    """
    list, int-> list
    :param matriz: Recebe lista de numeros inteiros
    :param n: Numero que irá ser multiplicada a matriz
    :param return: Retorna a matriz multiplicada pelo numero n 
    """
    linhas = range(len(matriz))
    colunas = range(len(matriz[0]))
    for multiplicacao in range(len(matriz)):
        matriz[linha][coluna] *=n

    return matriz



            
