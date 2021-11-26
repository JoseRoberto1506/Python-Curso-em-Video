'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = counter = cheaper = num_pro = 0
cheaper_product = ''

print("-" * 23)
print("      LOJA RECIFE")
print("-" * 23)

while True:
    product = str(input("Nome do Produto: ")).strip()
    price = float(input("Preço: R$ "))
    choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    num_pro += 1
    total += price

    if price > 1000:
        counter += 1
    
    if num_pro == 1:
        cheaper = price
        cheaper_product = product
    else:
        if price < cheaper:
            cheaper = price
            cheaper_product = product

    while choice not in 'SN':
        choice = str(input("Quer continuar? [S/N] ")).strip().upper()[0]   
    if choice == 'N':
        break

print("----------- FIM DO PROGRAMA -----------")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {counter} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {cheaper_product} que custa R${cheaper:.2f}")
