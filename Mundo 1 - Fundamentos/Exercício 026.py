# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

phrase = str(input("Digite uma frase: ")).strip().upper()

print(f"A letra A aparece {phrase.count('A')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {phrase.find('A') + 1}.")
print(f"A última letra A apareceu na posição {phrase.rfind('A') + 1}.")