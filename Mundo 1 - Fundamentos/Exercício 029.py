# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocity = float(input("Qual é a velocidade do carro em Km/h? "))

if velocity > 80:
    fine = (velocity - 80) * 7
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h.")
    print(f"Você deve pagar uma multa de R${fine:.2f}!")
 
print("Tenha um bom dia! Diriga com segurança!")