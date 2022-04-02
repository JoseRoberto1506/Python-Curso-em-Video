# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

players = {}
ranking = []
for c in range(1, 5):
    players[f"jogador_{c}"] = randint(1, 6)

print("Valores sorteados: ")
sleep(0.5)
for k, v in players.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(0.75)

print("=" * 45)
print("  == RANKING DOS JOGADORES ==  ")

ranking = sorted(players.items(), key = itemgetter(1), reverse = True)      
for i, v in enumerate(ranking):
    print(f"   {i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(0.75)
