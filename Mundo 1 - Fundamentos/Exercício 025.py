# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input("Qual é seu nome completo? ")).strip().upper()

print(f"Seu nome tem Silva? {'SILVA' in name}")