''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) 
e mostrá-lo por extenso.'''

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
           'dezoito', 'dezenove', 'vinte')

number = int(input("Digite um número entre 0 e 20: "))
while number not in range(0,21):
    number = int(input("Tente novamente. Digite um número entre 0 e 20: "))

print(f"Você digitou o número {numbers[number]}")
