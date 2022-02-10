'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = third_column = 0

for r in range(0,3):
    for c in range(0,3):
        matriz[r][c] = int(input(f"Digite um número para a posição [{r},{c}]: "))

        if matriz[r][c] % 2 == 0:
            even += matriz[r][c]

        if c == 2:
            third_column += matriz[r][c]

print('=' * 45)
for r in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[r][c]:^5}]", end='')
    print()

print(f"A soma dos valores pares é {even}.")
print(f"A soma dos valores da terceira coluna é {third_column}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}.")
