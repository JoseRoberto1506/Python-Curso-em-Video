# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for w in words:
    print(f"\nNa palavra {w} temos ", end='')
    for letter in w:
        if letter in 'AEIOU':
            print(letter, end=' ')
