def main():
    num1 = inteiro_1()
    num2 = inteiro_2()
    contador = 2
    while ((num1 % contador) != 0) or ((num2 % contador) != 0):
        contador += 1
    print(f'O MDC de {num1}, {num2} é : {contador}' )
        
        
def inteiro_1():
    while True:
        entrada = input('Digite o valor inteiro 1:')
        try:
            num = int(entrada)
            if num < 0:
                print('Valor não é inteirop positivo, digite outro!!!')
                return inteiro_1()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_1()
    
    
def inteiro_2():
    while True:
        entrada = input('Digite o valor inteiro 2:')
        try:
            num = int(entrada)
            if num < 0:
                print('Valor não é inteirop positivo, digite outro!!!')
                return inteiro_2()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro_2()
    

main()