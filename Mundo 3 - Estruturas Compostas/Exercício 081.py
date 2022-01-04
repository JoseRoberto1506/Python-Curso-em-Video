'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numbers = []

while True:
    numbers.append(int(input("Digite um valor: ")))
    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if answer == 'N':
        break

print("=" * 45)
print(f"Você digitou {len(numbers)} elementos")

numbers.sort(reverse=True)
print(f"Os valores em ordem decrescente são {numbers}")

if 5 in numbers:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
