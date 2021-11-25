def zodiaco(ano):
    """
    int->list
    :param ano: Entrada do ano de aniversario
    :return: O animal do zodiaco que representa o ano em que a pessoa nasceu
    """
    lista=["macaco","galo","cao","porco","rato","boi","tigre","coelho","dragao","serpente","cavalo","carneiro"]
    resultado=ano%12
    return lista[resultado]

#Testes
#teste1_1 = 1996 - resultado esperado "rato"
#teste1_2 = 1997 - resultado esperado "boi"
#teste1_3 = 1826 - resultado esperado "cao"
#teste1_4 = 1945 - resultado esperado "galo"