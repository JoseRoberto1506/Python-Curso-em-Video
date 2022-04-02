# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas; B) A média de idade; C) Uma lista com as mulheres; D) Uma lista de pessoas com idade acima da média

person = {}
people = []
answer = 'S'
women = []
tot = 0

while answer == 'S':
    person['nome'] = str(input("Nome: ")).strip()

    person['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while person['sexo'] not in "MF":
        print("ERRO! Por favor, digite apenas M ou F.")
        person['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if person['sexo'] == "F":
        women.append(person['nome'])
    
    person['idade'] = int(input("Idade: "))
    tot += person['idade']
    
    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while answer not in "SN":
        print("ERRO! Responda apenas S ou N.")
        answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    people.append(person.copy())
    average = tot / len(people)
    person.clear()

    if answer == 'N':
        break

print("=" * 60)
print(f"A) Ao todo temos {len(people)} pessoas cadastradas.")
print(f"B) A média de idade é de {average:5.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end=' ')
for m in women:
    print(m, end=' ')
print()
print("D) Lista das pessoas que estão acima da média:")
for p in people:
    if p['idade'] >= average:
        print('    ', end=' ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
