''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex:
print("Olá, Mundo!") Saída:
-----------
Olá, Mundo!
----------- '''

def write(txt):
    print("~" * (len(txt) + 4))
    print(f'  {txt}')
    print("~" * (len(txt) + 4))

write('Gustavo Guanabara')
write('Curso de Python no YouTube')
write("CeV")
