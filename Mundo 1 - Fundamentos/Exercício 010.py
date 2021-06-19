# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar Considere US$ 1,00 = R$ 3,27 

real = float(input("Quantos R$ você tem? R$"))
# Cotações atualizadas no dia 18/06/2021
dollar = real / 5.06
euro = real / 6.01
pound_sterling = real / 7

print(f"Com R${real:.2f} você pode comprar U${dollar:.2f}")
print(f"Com R${real:.2f} você pode comprar €{euro:.2f}")
print(f"Com R${real:.2f} você poe comprar £{pound_sterling:.2f}")