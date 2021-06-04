# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = float(input("Digite um número: "))
double = number * 2
triple = number * 3
square_root = number ** (1/2)

print(f"O dobro de {number} é {double}.")
print(f"O triplo de {number} é {triple}.")
print(f"A raíz quadrada de {number} é {square_root}.")
