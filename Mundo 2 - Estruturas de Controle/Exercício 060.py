# Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

print("Digite um número para")

number = int(input("Calcular seu Fatorial: "))
c = number

print(f"Calculando {number}! = ", end='')

while c > 0:
    print(c, end='')
    if c > 1:
        print(" x ", end='')
    else:
        print(" = ", end='')
    c -= 1

print(factorial(number))
