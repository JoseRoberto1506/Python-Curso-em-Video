# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

number = float(input("Digite um número: "))
whole_portion = trunc(number)

print(f"O número digitado foi {number} e a sua porção inteira é {whole_portion}.")