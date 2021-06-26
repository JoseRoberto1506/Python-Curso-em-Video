# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

sum = 0
counter = 0

for c in range(1, 7):
    number = int(input(f"Digite o {c}° valor: "))
    if number % 2 == 0:
        sum += number
        counter += 1

print(f"A soma dos {counter} valores pares digitados foi {sum}.")
