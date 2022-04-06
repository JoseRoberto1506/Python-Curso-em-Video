# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep

def greater(* num):
    print("=" * 60)
    print("Analisando os valores passados...")
    for n in numbers:
        print(n, end=' ', flush = True)
        sleep(0.5)
    print(f"Foram informados {len(numbers)} valores ao todo.")
    numbers.sort()
    print(f"O maior valor informado foi {numbers[-1]}.")

for c in range(0, 5):
    amount = randint(0, 9)
    numbers = []
    for c in range(0, amount + 1):
        numbers.append(randint(0, 10))
    greater(numbers)
