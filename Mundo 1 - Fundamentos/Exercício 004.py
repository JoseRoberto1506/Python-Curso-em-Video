# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

# O usuário digitará algo
a = input("Digite algo: ")

print(f"O tipo primtivo desse valor é: {type(a)}.")
print(f"Só tem espaços? {a.isspace()}.")
print(f"É um número? {a.isnumeric()}.")
print(f"É alfabético? {a.isalpha()}.")
print(f"Está em maiúsculas? {a.isupper()}.")
print(f"Está em minúsculas? {a.islower()}.")
print(f"Está capitalizado? {a.istitle()}.")