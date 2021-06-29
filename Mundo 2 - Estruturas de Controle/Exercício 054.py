# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

count_under_age = 0
count_over_age = 0

for people in range(1, 8):
    birth_year = int(input(f"Em que ano a {people}° pessoa nasceu? "))
    age = date.today().year - birth_year

    if age < 18:
        count_under_age += 1
    else:
        count_over_age += 1

print(f"Ao todo tivemos {count_over_age} pessoas maiores de idade.")
print(f"E também tivemos {count_under_age} pessoas menores de idade.")
