# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais. ISÓSCELES: dois lados iguais, um diferente. ESCALENO: todos os lados diferentes.

A = float(input("Primeiro segmento: "))
B = float(input("Segundo segmento: "))
C = float(input("Terceiro segmento: "))

if A < B + C and B < A + C and C < A + B:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end='')
    if A == B == C:
        print("EQUILÁTERO!")
    elif A == B != C or B == C != A or A == C != B:
        print("ISÓSCELES!")
    else:
        print("ESCALENO!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")
