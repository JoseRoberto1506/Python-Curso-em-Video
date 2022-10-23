# Função para calcular metade do preço
def metade(p=0, formatar=False):
    '''
    :param p: Preço
    :param formatar: Se True, retorna o preço formatado pela função moeda()
    :retorno: Metade do preço
    '''
    p = p / 2
    if (formatar == True):
        return moeda(p)
    else:
        return p

# Função que calcula o dobro do preço
def dobro(p=0, formatar=False):
    '''
    :param p: Preço
    :param formatar: Se True, retorna o preço formatado pela função moeda()
    :retorno: Dobro do Preço
    '''
    p = p * 2
    if (formatar == True):
        return moeda(p)
    else:
        return p

# Função que calcula um aumento de x% no preço
def aumentar(p=0, aumenta=0, formatar=False):
    '''
    :param p: Preço
    :param aumenta: Percentual de aumento
    :param formatar: Se True, retorna o preço formatado pela função moeda()
    :retorno: Preço + x%
    '''
    p = p + (p * (aumenta / 100))
    if (formatar == True):
        return moeda(p)
    else:
        return p

# Função que calcula uma diminuição de x%
def diminuir(p=0, diminui=0, formatar=False):
    '''
    :param p: Preço
    :param diminui: Percentual de diminuição
    :param formatar: Se True, retorna o preço formatado pela função moeda()
    :retorno: Preço - x%
    '''
    p = p - (p * (diminui / 100))
    if (formatar == True):
        return moeda(p)
    else:
        return p

# Função que mostra os valores monetários formatados
def moeda(p):
    '''
    :param p: Preço
    :retorno: Preço formatado como valor monetário
    '''
    return str(f"R${p:.2f}").replace(".", ",")
