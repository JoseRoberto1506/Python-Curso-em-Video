# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(w, l):
    a = w * l
    print(f"A área de um terreno {w:.2f} x {l:.2f} é de {a:.2f}m².")

print(f"{'Controle de Terrenos':^30}")
print("-" * 30)

width = float(input("LARGURA (m): "))
length = float(input("COMPRIMENTO (m): "))
area(width, length)
