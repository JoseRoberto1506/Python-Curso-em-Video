# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    number = int(input("Quer ver a tabuada de qual número? "))
    print("-" * 30)

    if number < 0:
        break

    c = 0
    for c in range(1,11):
        print(f"{number} x {c} = {number * c}")
        c += 1
    print("-" * 30)

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
