# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogos = []

jogador['nome'] = str(input("Nome do Jogador: ")).strip()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, partidas):
    jogos.append(int(input(f"   Quantos gols na partida {c}? ")))

jogador['gols'] = jogos
jogador['total'] = sum(jogos)

print("=" * 60)
print(jogador)
print("=" * 60)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("=" * 60)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

for i, v in enumerate(jogos):
    print(f"    => Na partida {i}, fez {v} jogos.")
print(f"Foi um total de {sum(jogos)} gols.")
