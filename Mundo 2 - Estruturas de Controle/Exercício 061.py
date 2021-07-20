# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("GERADOR DE PA")
print("=" * 15)

first_term = int(input("Primeiro termo: "))
rate = int(input("Razão da PA: "))
term = first_term
counter = 1

while counter < 11:
    print(f"{term} -> ", end='')
    term += rate
    counter += 1

print("FIM")
