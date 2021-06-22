# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO. Média entre 5.0 e 6.9: RECUPERAÇÃO. Média 7.0 ou superior: APROVADO.

grade1 = float(input("Primeira nota: "))
grade2 = float(input("Segunda nota: "))
grade3 = float(input("Terceira nota: "))
average = (grade1 + grade2 + grade3) / 3

print(f"A média do aluno é {average:.2f}.")

if average < 5:
    print("O aluno está REPROVADO.")
elif 5 <= average <= 6.9:
    print("O aluno está de RECUPERAÇÃO.")
else:
    print("O aluno está APROVADO.")
