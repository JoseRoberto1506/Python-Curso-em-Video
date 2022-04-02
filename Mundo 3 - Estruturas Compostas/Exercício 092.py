# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

datas = {}
from datetime import date

datas['Nome'] = str(input("Nome: ")).strip()
birth_year = int(input("Ano de nascimento: "))
datas['Idade'] = date.today().year - birth_year
datas['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if datas['CTPS'] != 0:
    datas['Contratação'] = int(input("Ano de Contratação: "))
    datas['Salário'] = float(input(f"Salário: R$"))
    datas['Aposentadoria'] = datas['Idade'] + ((datas['Contratação'] + 35) - date.today().year)

print("=" * 45)
for k, v in datas.items():
    print(f"  - {k} tem o valor {v}.")
