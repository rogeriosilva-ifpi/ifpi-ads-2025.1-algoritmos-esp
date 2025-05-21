def main():

    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    num = 1

    while b < (a+11):
        b = int(input('Digite novamente o valor de B: '))

    while a < b:
        while num <= a:
            if a % num == 0:
                print(f'Divisores de {a}: {num}')
                num += 1
            else:
                num += 1
        a += 1

main()