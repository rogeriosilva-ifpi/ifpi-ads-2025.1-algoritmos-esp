def receber_inteiro():
    numero = int(input('Digite seu número'))
    while numero != 0:
        numero = int(input('Digite outro número '))
        if numero >= 0:
            print('Este número é positivo')
        elif numero < 0:
            print('Este número é negativo')
            return receber_inteiro()

    def receber_numero(min,max):
        numero = int(input('Digite um número'))
        while numero == 0:
            if numero <= 500:
                min = numero
                print('Este é o valor minimo')
            elif numero > 500:
                max= numero
                print('Este é o nosso máximo valor')
            else:
                print('O valor está entre {} e {}'.format(min,max))

        




receber_inteiro()


# Um pouco confuso.



