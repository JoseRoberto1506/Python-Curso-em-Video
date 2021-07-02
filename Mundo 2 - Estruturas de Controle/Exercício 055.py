# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

list = []

for people in range(1, 6):
    weight = float(input(f"Peso da {people}° pessoa: "))
    list += [weight]

print(f"O maior peso lido foi de {max(list)}Kg.")
print(f"O menor pesso lido foi de {min(list)}Kg.")
