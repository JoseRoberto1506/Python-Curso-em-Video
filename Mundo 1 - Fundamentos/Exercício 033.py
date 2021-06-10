# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

value_1 = int(input("Primeiro valor: "))
value_2 = int(input("Segundo valor: "))
value_3 = int(input("Terceiro valor: "))

smaller = value_1
bigger = value_1

if value_2 < value_1 and value_2 < value_3:
    smaller = value_2
if value_3 < value_1 and value_3 < value_2:
    smaller = value_3

if value_2 > value_1 and value_2 > value_3:
    bigger = value_2
if value_3 > value_1 and value_3 > value_2:
    bigger = value_3

print(f"O menor valor digitado foi {smaller}.")
print(f"O maior valor digitado foi {bigger}.")