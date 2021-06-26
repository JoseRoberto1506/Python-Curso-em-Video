# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

sum = 0
counter = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        counter += 1
        sum += n

print(f"A soma de todos os {counter} valores solicitados é {sum}.")
