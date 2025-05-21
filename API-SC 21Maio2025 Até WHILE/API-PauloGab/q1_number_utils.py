def receber_int():
    try:
        inteiro = int(input(''))
        return inteiro
    except ValueError:
        while inteiro != int:
            inteiro = int(input(''))
        return inteiro

valor_teste = receber_int()


def int_positivo():
    inteiro = int(input(''))
    if inteiro < 0:
        a = 0