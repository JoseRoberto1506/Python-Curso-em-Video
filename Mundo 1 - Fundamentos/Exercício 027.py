# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input("Digite seu nome completo: ")).strip()
split_name = name.split()

print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {split_name[0]}.")
print(f"Seu último nome é {split_name[-1]}.")