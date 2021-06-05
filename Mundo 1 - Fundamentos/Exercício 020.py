# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

student_1 = str(input("Primeiro aluno: "))
student_2 = str(input("Segundo aluno: "))
student_3 = str(input("Terceiro aluno: "))
student_4 = str(input("Quarto aluno: "))

list = [student_1, student_2, student_3, student_4]
shuffle(list)

print(f"A ordem de apresentação será:\n{list}")