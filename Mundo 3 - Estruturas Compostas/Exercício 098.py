''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada '''

from time import sleep

def counter(f, e, s):
    print("=" * 45)
    print(f"Contagem de {f} até {e} de {s} em {s}")
    sleep(2.5)

    if s < 0:
        s *= -1
    if s == 0:
        s = 1

    if f < e:
        cont = f
        while cont <= e:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont += s
        print("FIM!")
    else:
        cont = f
        while cont >= e:
            print(cont, end=' ', flush=True)
            sleep(0.5)
            cont -= s
        print("FIM!")

counter(1, 10, 1)
counter(10, 0, 2)

print("=" * 45)
print("Agora é sua vez de personalizar a contagem!")
first = int(input("Início: "))
end = int(input("Fim: "))
step = int(input("Passo: "))
counter(first, end, step)
