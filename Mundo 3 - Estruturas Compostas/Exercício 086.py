# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for r in range(0,3):
    for c in range(0,3):
        matriz[r][c] = int(input(f"Digite um valor para [{r},{c}]: "))

print("=" * 45)
for r in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[r][c]:^5}]", end='')
    print()
