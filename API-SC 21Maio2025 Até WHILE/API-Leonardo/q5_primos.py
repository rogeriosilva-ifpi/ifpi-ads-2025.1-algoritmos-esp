def main():
    N = num_n()
    M = num_m()
    numeros = []
    while True:
        contador = N - 1
        while contador < M:
            numeros.append(contador)
            contador += 1
            print(contador) 
        break   
    ehprimo(numeros)
    
    
def num_n():
    while True:
        entrada = input('Digite o valor de N :')
        try:
            num = int(entrada)
            return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return num_n()


def num_m():
    while True:
        entrada = input('Digite o valor de M :')
        try:
            num = int(entrada)
            return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return num_m()
        
        
def ehprimo(numeros):
    num = len(numeros)
    while True:
        ...
main()