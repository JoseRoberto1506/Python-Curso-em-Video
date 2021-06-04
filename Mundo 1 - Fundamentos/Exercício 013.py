# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input("Qual é o salário do funcionário? R$"))
increase = salary + (salary * 15 / 100)

print(f"O funcionário que ganhava R${salary:.2f}, com 15% de aumento, passa a receber R${increase:.2f}.")