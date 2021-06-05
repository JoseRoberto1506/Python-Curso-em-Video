# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

student_1 = str(input("Primeiro aluno: "))
student_2 = str(input("Segundo aluno: "))
student_3 = str(input("Terceiro aluno: "))
student_4 = str(input("Quarto aluno: "))

list = [student_1, student_2, student_3, student_4]
chosen = choice(list)

print(f"O aluno escolhido foi {chosen}.")