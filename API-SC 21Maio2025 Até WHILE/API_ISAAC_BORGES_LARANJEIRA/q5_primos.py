from q1_number_utils import getPositiveInt

def ehPrimo(numero):
    if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0 :
        primoORnot = 'Primo'
    elif numero == 2 or numero == 3 or numero == 5 or numero == 7 :
        primoORnot = 'Primo'
    elif numero == 1 :
        primoORnot = 'Não Primo'
    else:
        primoORnot = 'Não Primo'

    return primoORnot


def main() :
    N = getPositiveInt('Digite um número (N) : ')
    M = getPositiveInt('Digite um número (M) : ')

    contador = N

    while contador <= M :
        primoORnot = ehPrimo(contador)
        print(f'[{contador:.0f}] {primoORnot}')
        contador += 1


main()