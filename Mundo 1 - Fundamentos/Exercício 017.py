# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cat_op = float(input("Comprimento do cateto oposto: "))
cat_adj = float(input("Cateto adjacente: "))
hypotenuse = hypot(cat_op, cat_adj)

print(f"A hipotenusa vai medir {hypotenuse:.2f}.")