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

print(f"O dobro de {number} é {double}.")
print(f"O triplo de {number} é {triple}.")
print(f"A raíz quadrada de {number} é {square_root}.")
