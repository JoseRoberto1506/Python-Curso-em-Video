# 

def leiaInt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return value

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
