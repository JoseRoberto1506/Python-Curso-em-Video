'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.'''

people = []
data = []
heaviest = lighter = 0

while True:
    data.append(str(input("Nome: ")))
    data.append(float(input("Peso (Kg): ")))

    if len(people) == 0:
        heaviest = lighter = data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1]
        if data[1] < lighter:
            lighter = data[1]

    people.append(data[:])
    data.clear()

    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if answer == 'N':
        break

print("=" * 45)
print(f"Ao todo, você cadastrou {len(people)} pessoas.")

print(f"O maior peso foi de {heaviest}Kg. Peso de ", end='')
for p in people:
    if p[1] == heaviest:
        print(f"[{p[0]}]", end=' ')

print(f"\nO menor peso foi de {lighter}Kg. Peso de ", end='')
for p in people:
    if p[1] == lighter:
        print(f"[{p[0]}]", end=' ')
