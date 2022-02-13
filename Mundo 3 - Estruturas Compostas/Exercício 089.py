# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

datas = []
aux = []

while True:
    aux.append(str(input("Nome: ")))
    aux.append(float(input("Nota 1: ")))
    aux.append(float(input("Nota 2: ")))
    datas.append(aux[:])
    aux.clear()

    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if answer == 'N':
        break

print("=" * 40)
print(f"{'Nº':<3} {'NOME':<15} {'MÉDIA':>5}")
print("-" * 25)

c = 0
for i in range(0, len(datas)):
    print(f"{i:<3} {datas[i][0]:<15} {((datas[i][1] + datas [i][2]) / 2):>5}")

print("-" * 25)

while True:
    i = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if i == 999:
        print("FINALIZANDO...")
        break
    
    if i <= len(datas) - 1:
        print(f"Notas de {datas[i][0]} são {datas[i][1:3]}")
        print("-" * 50)

print("<<< VOLTE SEMPRE >>>")
