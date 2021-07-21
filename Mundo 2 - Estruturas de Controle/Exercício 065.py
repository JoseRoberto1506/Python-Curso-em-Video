''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O 
programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

number = int(input("Digite um número: "))
choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
counter = 1
bigger = smaller = sum = number

while choice == 'S':
    number = int(input("Digite um número: "))
    choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    counter += 1
    sum += number
    average = sum / counter

    if number > bigger:
        bigger = number
    elif number < smaller:
        smaller = number 
    
print(f"Você digitou {counter} números e a média foi {average:.2f}.")
print(f"O maior valor foi {bigger} e o menor foi {smaller}.")
