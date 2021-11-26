''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo.'''

from random import randint

sum = counter = 0

print("=" * 30)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=" * 30)

while True:
    number = int(input("Digite um valor: "))
    choice = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]

    while choice not in 'PI':
        choice = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
        
    computer = randint(0,10)

    sum = number + computer

    if sum % 2 == 0:
        print("-" * 30)
        print(f"Você jogou {number} e o computador {computer}. Total de {sum} DEU PAR")
        print("-" * 30)
        if choice == 'P':
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=" * 30)
            counter += 1
        else:
            print("Você PERDEU!")
            break
    else:
        print("-" * 30)
        print(f"Você jogou {number} e o computador {computer}. Total de {sum} DEU ÍMPAR")
        print("-" * 30)
        if choice == 'I':
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print("=" * 30)
            counter += 1
        else:
            print("Você PERDEU!")
            break

print("=" * 30)
print(f"GAME OVER! Você venceu {counter} vezes.")
