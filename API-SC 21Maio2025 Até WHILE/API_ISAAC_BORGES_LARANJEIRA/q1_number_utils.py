def getInt(entrada):
    numero = float(input(entrada))
    #Colocando float para caso a entrada tenha numero decimal, 
    # não parar o programa abruptamente
    
    while numero % 1 != 0 :
        print('Entrada inválida!')
        numero = float(input(entrada))

    return numero

def getPositiveInt(entrada):
    numero = float(input(entrada))

    while numero % 1 != 0 or numero <= 0 :
        print('Entrada inválida!')
        numero = float(input(entrada))

    return numero

def getNegativeInt(entrada):
    numero = float(input(entrada))

    while numero % 1 != 0 or numero >= 0 :
        print('Entrada inválida!')
        numero = float(input(entrada))

    return numero

def getIntMin(entrada, min):
    numero = float(input(entrada))

    while numero % 1 != 0 or numero < min :
        print('Número invalido')
        numero = float(input(entrada))

    return numero

def getIntMax(entrada, max):
    numero = float(input(entrada))

    while numero % 1 != 0 or numero > max :
        print('Número invalido')
        numero = float(input(entrada))

    return numero

def getIntInRange(entrada, min, max):
    numero = float(input(entrada))

    while numero % 1 != 0 or numero < min or numero > max :
        print('Número Inválido!')
        numero = float(input(entrada))

    return numero

def main(): 
    pass

if __name__ == '__main__' :
    main()
