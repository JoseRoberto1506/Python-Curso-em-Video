# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = int(input("Informe um número: "))

unit = number // 1 % 10
set_of_ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10

print(f"Analisando o número {number}")
print(f"Unidade: {unit}")
print(f"Dezena: {set_of_ten}")
print(f"Centena: {hundred}")
print(f"Milhar: {thousand}")