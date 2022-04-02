# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

datas = {}

datas['name'] = str(input("Nome: "))
datas['average'] = float(input(f"Média de {datas['name']}: "))

print(f"Nome é igual a {datas['name']}")
print(f"Média é igual a {datas['average']}")

print("Situação é igual a ", end='')
if datas['average'] >= 7:
    print("Aprovado")
elif 5 <= datas['average'] < 7:
    print("Recuperação")
else:
    print("Reprovado")
