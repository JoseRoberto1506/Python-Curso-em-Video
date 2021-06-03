# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# O aluno digitará as uas notas
note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota: "))

# Variável para calcular a média
average = (note1 + note2) / 2

print(f"A média entre {note1} e {note2} é igual a {average:.2f}.")