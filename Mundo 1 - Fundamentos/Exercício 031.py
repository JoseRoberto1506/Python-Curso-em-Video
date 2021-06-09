# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distance = int(input("Qual é a distância da sua viagem em Km? "))

print(f"Você está prestes a começar uma viagem de {distance:.2f} Km.")

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

print(f"E o preço da sua passagem será de R${price:.2f}.")