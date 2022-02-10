# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

game = []

print("-" * 40)
print(f"{'JOGA NA MEGA SENA':^40}")
print("-" * 40)

total = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"=====  SORTEANDO {total} JOGOS  =====")

for c in range(1, total + 1):
    print(f"Jogo {c}: ", end='')
    
    for n in range(1,7):
        num = randint(1,60)
        if num not in game:
            game.append(num)

    sleep(1)
    game.sort()
    print(game)
    game.clear()

print("======   < BOA SORTE! >   ======")
