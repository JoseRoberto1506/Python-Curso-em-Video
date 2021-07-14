'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

value_1 = int(input("Primeiro valor: "))
value_2 = int(input("Segundo valor: "))

print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')

option = int(input("Qual é a sua opção? "))

while option != 5:

    if option == 1:
        sum = value_1 + value_2
        print(f"A soma entre {value_1} + {value_2} é {sum}.")

    elif option == 2:
        multiplication = value_1 * value_2
        print(f"O resultado de {value_1} x {value_2} é {multiplication}.")

    elif option == 3:
        if value_1 > value_2:
            bigger = value_1
        elif value_2 > value_1:
            bigger = value_2
        print(f"Entre {value_1} e {value_2} o maior valor é {bigger}")

    elif option == 4:
        print("Informe os números novamente:")
        value_1 = int(input("Primeiro valor: "))
        value_2 = int(input("Segundo valor: "))

    else:
        print("Opção inválida. Tente novamente.")

    print("=" * 30)
    sleep(3)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')

    option = int(input("Qual é a sua opção? "))

print("Finalizando...")
print("=" * 30)
sleep(3)
print("Fim do programa! Volte sempre!")
