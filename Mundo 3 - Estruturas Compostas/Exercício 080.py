# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numbers = []

for c in range(0, 5):
    number = int(input("Digite um valor: "))

    if c == 0 or number > numbers[-1]:
        numbers.append(number)
    else:
        pos = 0
        while pos < len(numbers):
            if number <= numbers[pos]:
                numbers.insert(pos, number)
                break
            pos += 1

print(f"Os valores digitados em ordem foram {numbers}")
