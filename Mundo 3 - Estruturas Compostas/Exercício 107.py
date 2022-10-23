'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from utilidadesCeV import moeda

price = float(input("Digite o preço: R$"))
print(f"A metade de {price} é {moeda.metade(price)}")
print(f"O dobro de {price} é {moeda.dobro(price)}")
print(f"Aumentando 10%, temos {moeda.aumentar(price, 10)}")
print(f"Diminuindo 15%, temos {moeda.diminuir(price, 15)}")
