'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado'''

from utilidadesCeV import moeda

price = float(input("Digite o preço: R$"))
print(f"A metade de {moeda.moeda(price)} é {moeda.moeda(moeda.metade(price))}")
print(f"O dobro de {moeda.moeda(price)} é {moeda.moeda(moeda.dobro(price))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(price, 10))}")
print(f"Diminuindo 15%, temos {moeda.moeda(moeda.diminuir(price, 15))}")
