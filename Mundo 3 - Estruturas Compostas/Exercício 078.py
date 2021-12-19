# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

values = []
for i in range(0, 5):
    values.append(int(input(f"Digite um valor para a Posição {i}: ")))

print("=" * 45)
print(f"Você digitou os valores {values}")

print(f"O maior valor digitado foi {max(values)} nas posições ", end='')
for i, v in enumerate(values):
    if v == max(values):
        print(f"{i}...", end='')

print(f"\nO menor valor digitado foi {min(values)} nas posições ", end='')
for i, v in enumerate(values):
    if v == min(values):
        print(f"{i}...", end='')

print()
