# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# O usuário digitará um número
number = int(input("Digite um número: "))

# Variável para o cálculo do sucessor
sucessor = number + 1

# Varável para o cáculo do antecessor
predecessor = number - 1

print(f"O antecessor do número {number} é {predecessor} e seu sucessor é {sucessor}")