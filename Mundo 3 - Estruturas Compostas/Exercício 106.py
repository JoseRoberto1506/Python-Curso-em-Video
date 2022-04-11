# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep

c = ('\033[m', # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m' # 6 - branco
    )

def search(op):
    title(f"Acessando o manual do comando '{option}'", 4)
    print(c[6], end='')
    help(op)
    print(c[0],end='')
    sleep(2)

def title(msg, color = 0):
    print(c[color], end='')
    print("~" * (len(msg) + 4))
    print(f"  {msg}")
    print("~" * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)

option = ''
while True:
    title("SISTEMA DE AJUDA PyHELP", 2)
    option = str(input("Função ou Biblioteca: ")).strip()
    if option.upper() == "FIM":
        break
    else:
        search(option)
title("ATÉ LOGO!", 1)
