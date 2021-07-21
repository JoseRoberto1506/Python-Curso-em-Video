# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

total_terms = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
counter = 3

print(f"{t1} -> {t2} -> ", end='')

while counter <= total_terms:
    t3 = t1 + t2
    print(f"{t3} -> ", end='')
    t1 = t2
    t2 = t3
    counter += 1

print("FIM")
