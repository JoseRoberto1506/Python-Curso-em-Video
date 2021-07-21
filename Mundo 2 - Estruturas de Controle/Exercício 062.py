# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

first_term = int(input("Primeiro termo: "))
rate = int(input("Razão da PA: "))
term = first_term
counter = 1
more = 10
total = 0

while more != 0:
    total += more
    while counter <= total:
        print(f"{term} -> ", end='')
        term += rate
        counter += 1
    print("PAUSA")
    more = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total} termos mostrados.")
