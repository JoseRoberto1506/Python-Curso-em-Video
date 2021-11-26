''' Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

sum = counter = 0

while True:
    value = int(input("Digite um valor (999 para parar): "))
    if value == 999:
        break
    sum += value
    counter += 1

print(f"A soma dos {counter} valores foi {sum}!")
