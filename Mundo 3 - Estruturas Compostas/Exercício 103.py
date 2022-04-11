# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def record(name = '<desconhecido>', goals = 0):
    print(f"O jogador {name} fez {goals} gol(s) no campeonato.")

print("-" * 45)
player = str(input("Nome do jogador: ")).strip()
score = str(input("Número de gols: "))
if score.isnumeric():
    score = int(score)
else:
    score = 0
if player == '':
    record(goals=score)
else:
    record(player, score)
