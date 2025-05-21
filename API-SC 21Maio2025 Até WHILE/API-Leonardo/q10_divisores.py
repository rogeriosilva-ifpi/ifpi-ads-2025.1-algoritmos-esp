def main():
    B = num_b()
    A = num_a()
    while True:
        if B < A in range(11):
            break
        while A <= B:
            # divisor = divisores(A)
            A +=1
            print(A)
            
            
    

def num_b():
    while True:
        entrada = input('Digite o valor de b :')
        try:
            num = int(entrada)
            if num < 0:
                print('Valor não é inteirop positivo, digite outro!!!')
                return num_b()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return num_b()
        
        
def num_a():
    while True:
        entrada = input('Digite o valor de a :')
        try:
            num = int(entrada)
            if num < 0:
                print('Valor não é inteirop positivo, digite outro!!!')
                return num_a()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return num_a()
        
        
def divisores(A):
    contador = 1
    qtd_divisores = 0
    while A / contador != 0:
        if A == 0:
            return A
        contador+=1
        qtd_divisores +=1
    return qtd_divisores
        
        
main()