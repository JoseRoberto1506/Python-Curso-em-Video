# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input("Em que cidade você nasceu? ")).strip().upper()

division = city.split()

print("SANTO" in division[0])