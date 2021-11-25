

#Maria Luiza Lino de Souza
#DRE:119162682

#Questão 1
def novo_contato(nome, numero, email, instagram):
    numero = [numero]
    return [nome, numero, email, instagram]

#atualiza contato
def atualiza_contato(contato, tipo, informacao):
    if tipo != 1 and tipo < 4:
        contato[tipo] = informacao 
        return True
    elif tipo == 1:
        if informacao in contato[tipo]:
            contato[tipo].remove(informacao)
            return False
        else:
            contato[tipo].append(informacao)
            return True
    else:
        return False

#Teste cria contato e altera dados
#Cria contato
#contato = novo_contato('Pedro','123456678','pedrinho24@gmail.com','pedrinho23')
#resultado obtido:['Pedro', ['123456678'], 'pedrinho24@gmail.com', 'pedrinho23']

#Atualiza nome
#atualiza_contato(contato, 0, 'Joao')
#resultado obtido:['Joao', ['123456678'], 'pedrinho24@gmail.com', 'pedrinho23']

#Adiciona numero
#atualiza_contato(contato, 1, '2234423242')
#resultado obtido:['Joao', ['123456678', '2234423242'], 'pedrinho24@gmail.com', 'pedrinho23']

#Remove número
#atualiza_contato(contato, 1, '2234423242')
#resultado obtido:['Joao', ['123456678'], 'pedrinho24@gmail.com', 'pedrinho23']

#atualiza email
#atualiza_contato(contato, 2, 'pedrinho66@gmail.com')
#resultado obtido:['Joao', ['123456678'], 'pedrinho66@gmail.com', 'pedrinho23']

#atualiza instagram
#atualiza_contato(contato, 3, 'pedro23')
#resultado obtido:['Joao', ['123456678'], 'virgula', 'pedro23']

#Tenta atualizar informacao q nao existe
#alterado = atualiza_contato(contato, 4, 'golf')
#resultado obtido:False

#Teste Lista de contatos
#Lista_de_contatos = [ novo_contato('Pedro','123456678','opiwsjiajofajfi','jsnbajsaja'), novo_contato('Luiz','3846832','hdgfjskl','aasfa')]
#Contato 1
#Lista_de_contatos[0]
#resultado obtido:['Pedro', ['123456678'], 'pedrinho24@gmail.com', 'pedrinho23']
#Contato 2
#Lista_de_contatos[1]
#resultado obtido:['Luiz', ['3846832'], 'luiz@gmail.com', 'Luluiz']


#Adiciona numero 12313 ao contato 1
#atualiza_contato(Lista_de_contatos[0], 1, '12313')
#resultado obtido:['Pedro', ['123456678', '12313'], 'pedrinho24@gmail.com', 'pedrinho23']

#Altera o email (anaoperneta) do contato 2
#atualiza_contato(Lista_de_contatos[1], 2, "luiz@hotmail.com")
#resultado obtido:['Luiz', ['3846832'], luiz@hotmail.com, 'Luluiz']

