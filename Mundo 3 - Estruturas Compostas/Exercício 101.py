# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def vote(year):
    from datetime import date
    age = date.today().year - year
    
    if 16 <= age < 18 or age > 70:
        return f"Com {age} anos: VOTO OPCIONAL."
    elif 18 <= age <= 70:
        return f"Com {age} anos: VOTO OBRIGATÓRIO."
    else:
        return f"Com {age} anos: NÃO VOTA."
    
print("-" * 30)
birth_year = int(input("Em que ano você nasceu? "))
print(vote(birth_year))
