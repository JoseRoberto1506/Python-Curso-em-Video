# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar Considere US$ 1,00 = R$ 3,27 

real = float(input("Quantos R$ você tem? R$"))

dollar = real / 3.7

print(f"Com R${real:.2f} você pode comprar U${dollar:.2f}")