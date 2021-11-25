'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

older = men = women = 0

while True:
    print("-" * 31)
    print("      CADASTRE UMA PESSOA")
    print("-" * 31)

    age = int(input("Idade: "))
    sex = str(input("Sexo: [M/F] ")).strip().upper()[0]

    while sex not in "MF":
        sex = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if age > 18:
        older += 1
    
    if sex == 'M':
        men += 1

    if sex == 'F':
        if age < 20:
            women += 1

    print("-" * 31)

    choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    
    while choice not in "SN":
        choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if choice == 'N':
        break

print("======  FIM DO PROGRAMA ======")
print(f"Total de pessoas com mais de 18 anos: {older}")
print(f"Ao todo temos {men} homens cadastrados")
print(f"E temos {women} mulheres com menos de 20 anos")
