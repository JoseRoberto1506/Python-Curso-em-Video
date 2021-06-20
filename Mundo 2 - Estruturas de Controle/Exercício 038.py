# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais.

number1 = float(input("Primeiro número: "))
number2 = float(input("Segundo número: "))

if number1 > number2:
    print("O PRIMEIRO valor é maior.")
elif number2 > number1:
    print("O SEGUNDO valor é maior.")
else:
    print("Os dois valores são IGUAIS.")
