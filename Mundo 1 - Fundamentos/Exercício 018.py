# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angle = float(input("Digite o ângulo que você deseja: "))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print(f"O ângulo de {angle} tem o SENO de {sine:.2f}.")
print(f"O ângulo de {angle} tem o COSSENO de {cosine:.2f}.")
print(f"O ângulo de {angle} tem a TANGENTE de {tangent:.2f}.")