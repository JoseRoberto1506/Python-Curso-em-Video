''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– 2x no cartão: preço normal 
– 3x ou mais no cartão: 20% de juros'''

price = float(input("Preço das compras: R$"))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

option = int(input("Qual é a opção? "))

if option in [1, 2, 3, 4]:
    if option == 1:
        new_price = price - (price * 0.1)
    elif option == 2:
        new_price = price - (price * 0.05)
    elif option == 3:
        installment = price / 2
        new_price = price
        print(f"Sua compra será parcelada em 2x de R${installment:.2f} SEM JUROS.")
    elif option == 4:
        installment = int(input("Quantas parcelas? "))
        new_price = (price + (price * 0.2)) / installment
        print(f"Sua compra será parcelada em {installment}x de R${new_price:.2f} COM JUROS.")
    print(f"Sua compra de R${price:.2f} vai custar R${new_price:.2f} no final.")
else:
    print("Opção inválida. Tente novamente.")
