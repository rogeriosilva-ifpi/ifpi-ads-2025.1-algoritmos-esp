def main():
    num_inteiro = inteiro()
    num_inteiro_positivo = inteiro_positivo()
    num_inteiro_negativo = inteiro_negativo()
    num_inteiro_minimo = inteiro_minimo()
    num_inteiro_maximo = inteiro_maximo()
    num_inteiro_faixa = inteiro_faixa()
    
    
def inteiro():
    while True:
        entrada = input('Digite o valor inteiro :')
        try:
            num = int(entrada)
            return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro()


def inteiro_positivo():
    while True:
        entrada = input('Digite o valor inteiro positivo :')
        try:
            num = int(entrada)
            if num < 0:
                print('Valor não é inteirop positivo, digite outro!!!')
                return inteiro_positivo()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_positivo()
        
        
def inteiro_negativo():
    while True:
        entrada = input('Digite o valor inteiro negativo :')
        try:
            num = int(entrada)
            if num > 0:
                print('Valor não é inteiro negativo, digite outro!!!')
                return inteiro_negativo()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_negativo()
        
        
def inteiro_minimo():
    while True:
        entrada = input('Digite o valor inteiro :')
        minimo = input('Digite o minimo : ')
        try:
            num = int(entrada)
            min = int(minimo)
            if (num < min):
                print('Valor não é inteiro é menor que o minimo, digite outro!!!')
                return inteiro_minimo()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_minimo()
    
    
def inteiro_maximo():
    while True:
        entrada = input('Digite o valor inteiro :')
        maximo= input('Digite o maximo : ')
        try:
            num = int(entrada)
            max = int(maximo)
            if (num > max):
                print('Valor não é inteiro é maior que o maximo, digite outro!!!')
                return inteiro_maximo()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_maximo()
    
    
def inteiro_faixa():
    while True:
        entrada = input('Digite o valor inteiro :')
        maximo= input('Digite o maximo : ')
        minimo = input('Digite o minimo : ')
        try:
            num = int(entrada)
            max = int(maximo)
            min = int(minimo)
            if (num > max) and (num < min):
                print('Valor não é inteiro não está na faixa, digite outro!!!')
                return inteiro_maximo()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_maximo()
    
    
main()