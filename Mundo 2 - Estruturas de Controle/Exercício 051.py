# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

first_term = int(input("Primeiro termo: "))
rate = int(input("Razão: "))
tenth = first_term + (10 - 1) * rate

for c in range(first_term, tenth + rate, rate):
    print(f"{c} ->", end=' ')

print("ACABOU")
