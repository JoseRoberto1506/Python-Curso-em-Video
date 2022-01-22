# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numbers = [[], []]

for c in range(1,8):
    number = int(input(f"Digite o {c}º valor: "))

    if number % 2 == 0:
        numbers[0].append(number)
        numbers[0].sort()
    else:
        numbers[1].append(number)
        numbers[1].sort()

print("=" * 50)
print(f"Os valores pares digitados foram: {numbers[0]}")
print(f"Os valores ímpares digitados foram: {numbers[1]}")
