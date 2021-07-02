# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

sum_age = 0
older = 0
count_woman = 0

for people in range(1, 5):
    print(f"----- {people}° PESSOA -----")
    name = str(input("Nome: ")).strip()
    age = int(input("Idade: "))
    sex = str(input("Sexo [M/F]: ")).strip().upper()

    sum_age += age
    age_average = sum_age / 4

    if sex == 'M':
        age_man = age 
        if age_man > older:
            older = age_man
            older_man = name

    if sex == 'F':
        age_woman = age
        if age_woman < 20:
            count_woman += 1

print(f"A média de idade do grupo é de {age_average:.1f} anos.")
print(f"O homem mais velho tem {older} anos e se chama {older_man}.")
print(f"Ao todo são {count_woman} mulheres com menos de 20 anos.")
