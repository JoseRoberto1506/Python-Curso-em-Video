# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

# O usuário digitará um número
number = float(input("Digite um número: "))

# Variável para calcular o dobro do número
double = number * 2

# Variável para calcular o triplo do número
triple = number * 3

# Variável para calcular a raíz quadrada
square_root = math.sqrt(number)

print(f"O dobro do número digitado é {double}.")
print(f"O triplo do número digitado é {triple}.")
print(f"A raíz quadrada o número digitado é {square_root}.")