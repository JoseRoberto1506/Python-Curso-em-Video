''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares 
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

numbers = []
even = []
odd = []

while True:
    numbers.append(int(input("Digite um número: ")))
    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if answer == 'N':
        break

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("=" * 45)
print(f"A lista completa é {numbers}")
print(f"A lista de pares é {even}")
print(f"A lista de ímpares é {odd}")
