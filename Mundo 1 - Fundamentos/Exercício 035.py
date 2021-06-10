# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("-" * 28)
print("| Analisador de triângulos |")
print("-" * 28)

A = float(input("Primeiro segmento: "))
B = float(input("Segundo segmento: "))
C = float(input("Terceiro segmento: "))

if A < B + C and B < A + C and C < A + B:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
