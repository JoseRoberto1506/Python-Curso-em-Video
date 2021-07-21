# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

number = sum = total_numbers = 0

while number != 999:
    number = int(input("Digite um número [999 para parar]: "))
    sum += number
    total_numbers += 1
    total_sum = sum - 999

print(f"Você digitou {total_numbers - 1} números e a soma entre eles foi {total_sum}.")
