# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços), quantas letras tem o primeiro nome.

name = str(input("Digite seu nome completo: ")).strip()
split_name = name.split()

print(f"Analisando seu nome...")
print(f"Seu nome em maiúsculas é {name.upper()}.")
print(f"Seu nome em minúsculas é {name.lower()}.")
print(f"Seu nome tem ao todo {len(name.replace(' ',''))} letras.")
print(f"Seu primeiro nome é {split_name[0]} e ele tem {len(split_name[0])} letras.")