# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input("Digite um número: "))
counter = 0

for c in range(1, number + 1):
    if number % c == 0:
        counter += 1

print(f"O número {number} foi divisível {counter} vezes.")

if counter == 2:
    print("E por isso ele É PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
