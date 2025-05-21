#Letra A


def numero_interio():

    while True:
        numero = int(input('Digite um número inteiro: '))
        print(f'{numero} é um número inteiro!')
        return numero
    

resultado = numero_interio()
print(f'{resultado} é um número interio')

#Letra B


def numero_interio_positivo():

    while True:
        numero = int(input('Digite um número inteiro positivo: '))
        if numero > 0:
            print(f'{numero} é um número inteiro positivo!')
            return numero
        print(f'{numero} não é um número interio positivo!')

resultado = numero_interio_positivo()
print(f'{resultado} é um número interio positivo')

#Letra C

def numero_interio_negativo():

    while True:
        numero = int(input('Digite um número inteiro negativo: '))
        if numero < 0:
            print(f'{numero} é um número inteiro negativo!')
            return numero
        print(f'{numero} não é um número interio negativo!')

resultado = numero_interio_negativo()
print(f'{resultado} é um número interio negativo')

#Letra D

def numero_minimo():


    numero_fixo = 5

    while True:
        numero = int(input(f'Digite um número inteiro maio ou igual a {numero_fixo}: '))
        if numero >= numero_fixo:
            print(f'{numero} é um valor aceito!')
            return numero
        print(f'{numero} é menor que o valor minimo {numero_fixo}, digite novamente')
        
resultado = numero_minimo()
print(resultado)
    

#Letra E

def numero_maximo():



    numero_maximo = int(input('Digite um número: '))


    while True:
        numero = int(input(f'Digite um número menor ou igual a {numero_maximo}: '))
        if numero <= numero_maximo:
            print(f'{numero} é um número válido!')
            return numero
        print(f'{numero} é invalido, digite novamente')

resultado = numero_maximo()
print(resultado)

#Letra F


def numero_faixa():


    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um número: '))


    while True:
        numero = int(input(f'Digite um número entre {numero_1} e {numero_2}: '))
        if numero >= numero_1 and numero <= numero_2 or numero >= numero_2 and numero <= numero_1:
            print(f'{numero} está entre {numero_1} e {numero_2}')
            return numero
        print(f'{numero} não está entre o número {numero_1} e {numero_2},digite novamente')

resultado = numero_faixa()
print(resultado)
