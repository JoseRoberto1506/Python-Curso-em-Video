''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se 
alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

birth_year = int(input("Ano de nascimento: "))
sex = str(input("Qual o seu sexo? [M/F] ")).strip().upper()
year = date.today().year
age = year - birth_year

print(f"Quem nasceu em {birth_year} tem {age} anos em {year}.")

if sex == 'M':
    if age < 18:
        print(f"Ainda faltam {18 - age} anos para o alistamento.")
        print(f"Seu alistamento será em {year + (18 - age)}.")
    elif age == 18:
        print("Você tem que se alistar IMEDIATAMENTE!")
    else:
        print(f"Você já deveria ter se alistado há {age - 18} anos.")
        print(f"Seu alistamento foi em {year - (age - 18)}.")
elif sex == 'F':
    print("Você não precisa fazer o alistamento militar obrigratório.")

else:
    print("Opção inválida.")
