# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = int(input("Valor da casa: R$"))
salary = float(input("Salário do comprador: R$"))
financing = int(input("Quantos anos de financiamento? "))
installment = house_value / (financing * 12)

print(f"Para pagar uma casa de R${house_value:.2f} em {financing} anos a prestação será de R${installment:.2f}")

if installment <= salary * 0.3:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")