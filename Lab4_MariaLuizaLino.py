
#Maria Luiza Lino de Souza
#DRE 119162682

#Questão 1


def Siga(tupla):
    """
    str->tupla
    :param return: Ele retorna com base nos inputs se o aluno está aprovado ou não.
    """
    nome = tupla[0]
    media = (tupla[1] + tupla [2] + tupla[3])/3
    if media >=7:
        return (nome,"%.2f" % media, "aprovado", "Parabens!")
    elif media >=5:
        return (nome,"%.2f" % media, "aprovado")
    else:
        return (nome, "%.2f" % media, "reprovado")


#Testes realizados:
#teste1_1 = Siga(("Rodrigo", 4.5,7.0,3.4)) - ('Rodrigo', '4.97', 'reprovado')
#teste1_2 = Siga(("Luiz",2.2,1.4,10.0)) - ('Luiz', '4.53', 'reprovado')
#teste1_3 = Siga(("Malu",10.0, 9.0, 7.9)) - ('Malu', '8.97', 'aprovado', 'Parabens!')
#teste1_4 = Siga(("Daniel", 9.9, 5.6,8.9)) - ('Daniel', '8.13', 'aprovado', 'Parabens!')


#Questão 2

def formato_data():
    """
    str->tupla
    :param return: identifica o formato da data dada como entrada, com base
    nos valores dos componentes da data: dd/mm/yy, mm/dd/yy, yy/mm/dd
    """

    comp1 = int(data[:2])
    comp2 = int(data[3:5])
    comp3 = int(data[6:])
    formatos = ()

    if (1 <= comp1 <= 31 and 1 <= comp2 <= 12):
        formatos += ("dd/mm/yy",)
    if (1 <= comp1 <= 12 and 1 <= comp2 <= 31):
        formatos += ("mm/dd/yy",)
    if (1 <= comp2 <= 12 and 1 <= comp3 <= 31):
        formatos += ("yy/mm/dd",)

    return formatos

#Testes realizados:
#teste2_1 = formato_data("98/25/07") == tuple()
#teste2_2 = formato_data("01/01/00") == ("dd/mm/yy", "mm/dd/yy")
#teste2_3 = formato_data("00/10/01") == ("yy/mm/dd",)
#teste2_4 = formato_data("01/01/01") == ("dd/mm/yy", "mm/dd/yy", "yy/mm/dd")






