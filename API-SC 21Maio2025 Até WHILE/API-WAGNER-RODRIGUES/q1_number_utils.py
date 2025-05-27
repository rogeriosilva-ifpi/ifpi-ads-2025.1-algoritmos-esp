#Funções

def pedir_numero_inteiro(numero):
    while(numero <= 0 ):
        numero_inteiro = int(input("Digite um número inteiro"))
        return numero_inteiro
    


def pedir_numero_positivo(numero):
    while (numero < 0):
        numero_positivo = int(input("Digite um número inteiro"))
        return numero_positivo
    

def pedir_numero_negativo(numero):
    while (numero > 0):
        numero_negativo = int(input("Digite um número inteiro"))
        return numero_negativo


def pedir_numero_minimo(numero, minimo):
    while (numero < minimo):
        numero_minimo = int(input("Digite um número maior: "))


def pedir_numero_maximo(numero, maximo):
    while (numero > maximo):
        numero_minimo = int(input("Digite um número menor: "))


def pedir_numero_minimo_maximo(numero, minimo,maximo):
    while (numero < minimo and numero > maximo):
        numero_minimo = int(input("Digite outro número: "))


# Faltou entender melhor a questão. 