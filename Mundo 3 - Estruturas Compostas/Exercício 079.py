''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

numbers = []

while True:
    number = int(input("Digite um número: "))

    if number not in numbers:
        numbers.append(number)
        print("Valor adicionado com sucesso...")
        answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    else:
        print("Valor duplicado! Não vou adicionar...")
        answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]    
    if answer == 'N':
        break

print("=" * 40)
print(f"Você digitou os valores {sorted(numbers)}")
