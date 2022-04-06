# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def raffle(num):
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(0, 5):
        num.append(randint(0, 10))
    for n in num:
        print(n, end=' ', flush = True)
        sleep(0.5)
    print("PRONTO!")

def EvenSum(num):
    sum = 0
    for n in num:
        if n % 2 == 0:
            sum += n
    print(f"Somando os valores pares de {num}, temos {sum}")

numbers = []
raffle(numbers)
EvenSum(numbers)
