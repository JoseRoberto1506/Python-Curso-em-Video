''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas;
– A menor nota ;
– A média da turma;
– A situação (opcional).'''

def grades(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos;
    :param n: Uma ou mais notas dos alunos (aceita várias);
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação;
    :return: Dicionário com várias informações sobre a situação da turma.
    '''
    a = {}
    c = greater = smaller = 0

    print("-" * 50)
    a['total'] = len(num)
    average = sum(num) / len(num)

    for n in num:
        if c == 0:
            greater = smaller = n
        else:
            if n > greater:
                greater = n
            if n < smaller:
                smaller = n
        c += 1
    a['maior'] = greater
    a['menor'] = smaller
    a['média'] = average

    if sit:
        if average >= 7:
            a['situação'] = 'BOA'
        elif 5 <= average < 7:
            a['situação'] = 'RAZOÁVEL'
        else:
            a['situação'] = 'RUIM'
    return a

answer = grades(5.5, 8, 9, sit=True)
print(answer)
help(grades)
