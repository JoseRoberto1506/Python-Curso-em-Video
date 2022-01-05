# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input("Digite a expressão: "))
a = []

for character in expression:
    if character == "(":
        a.append("(")
    elif character == (")"):
        if len(a) > 0:
            a.pop()
        else:
            a.append(")")
            break

if len(a) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
