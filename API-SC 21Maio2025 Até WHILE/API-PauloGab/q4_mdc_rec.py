def main():
    num1, num2 = receber_num()
    resultado = verificar_divisores(num1, num2)
    print(resultado)

def receber_num():
    a = int(input(''))
    b = int(input(''))
    return a, b

def verificar_divisores(a, b):
    if a < b:
        if a % a == 0 and b % a == 0:
            return a
        else:
            return verificar_divisores(a-1, b)
    elif b < a:
        if a % b == 0 and b % b == 0:
            return b
        else:
            return verificar_divisores(a, b-1)


main()