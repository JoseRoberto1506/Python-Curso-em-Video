'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10. 
Será que você consegue adivinhar qual foi?''')

counter = 1
number = randint(0, 10)
guess = int(input("Qual é seu palpite? "))

while guess != number:
    if guess < number:
        print("Mais... Tente mais uma vez.")
    elif guess > number:
        print("Menos... Tente mais uma vez.")

    guess = int(input("Qual é seu palpite? "))
    counter += 1

print(f"Acertou com {counter} tentativas. Parabéns!")
