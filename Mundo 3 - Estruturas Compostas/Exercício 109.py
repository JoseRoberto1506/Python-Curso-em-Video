'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from utilidadesCeV import moeda

price = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(price)} é {moeda.metade(price, True)}")
print(f"O dobro de {moeda.moeda(price)} é {moeda.dobro(price, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(price, 10, True)}")
print(f"Diminuindo 15%, temos {moeda.diminuir(price, 15, True)}")
