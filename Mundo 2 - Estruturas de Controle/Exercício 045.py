# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import choice

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

player = int(input("Qual é a sua jogada? "))

if player in [0, 1, 2]:
    if player == 0:
        player = 'Pedra'
    elif player == 1:
        player = 'Papel'
    elif player == 2:
        player = 'Tesoura'

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")

    computer = choice(['Pedra', 'Papel', 'Tesoura'])

    print("=" * 25)
    print(f"Computador jogou {computer}")
    print(f"Jogador jogou {player}")
    print("=" * 25)

    # Jogador vence
    if player == 'Pedra' and computer == 'Tesoura':
        print("JOGADOR VENCE")
    elif player == 'Papel' and computer == 'Pedra':
        print("JOGADOR VENCE")
    elif player == 'Tesoura' and computer == 'Papel':
        print("JOGADOR VENCE")

    # Empate
    elif player == computer:
        print("EMPATE")

    # Computador vence
    elif computer == 'Pedra' and player == 'Tesoura':
        print("COMPUTADOR VENCE")
    elif computer == 'Papel' and player == 'Pedra':
        print("COMPUTADOR VENCE")
    elif computer == 'Tesoura' and player == 'Papel':
        print("COMPUTADOR VENCE")
else:
    print("JOGADA INVÁLIDA")
