def readPrice(msg):
    valid = False
    while True:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f"\033[0;31mERRO: '{p}' é um preço inválido!\033[m")
        else:
            valid = True
            return float(p)
