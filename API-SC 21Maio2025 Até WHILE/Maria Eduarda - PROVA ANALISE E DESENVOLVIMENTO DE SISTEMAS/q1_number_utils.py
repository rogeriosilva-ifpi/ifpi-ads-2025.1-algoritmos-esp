
#funções

 #receber numero inteiro:

def receber_num_inteiro():
    while True:
        try:
            num = int(input('Por favor digite um numero: '))
            return num
        except  ValueError:
            print('O valor que você digitou é invalido!') 
            
numero = receber_num_inteiro()
print(f'{numero}') 
         
#receber numero inteiro positivo 

def numero_positivo():
    
    num = int(input('Por favor digite um numero inteiro positivo10: '))
    if num > 0:
        return num
    else:   
        return 'O valor que você digitou é invalido!' 

numero = numero_positivo()
print(f'{numero}')

#receber numero inteiro negativo

def num_negativo(): 
    num = int(input('Por favor digite um numero negativo: '))
    if num < 0:
        return num
    else:   
        return'O valor que você digitou é invalido!'

numero = num_negativo()
print(f'{numero}')

#receber numero inteiro de no minimo x

def min_numero():
    minimo = int(input('Por favor digite um numero minimo: ')) 
    num = int(input('Por favor digite um numero: '))
    
    if num > minimo:
        return num
    else:   
        return'O valor que você digitou é invalido!'

numero = min_numero()
print(f'{numero}')

#receber numero inteiro de no maximo x 

def max_num():
    maximo = int(input('Por favor digite um numero maximo: ')) 
    num = int(input('Por favor digite um numero: '))
    
    if maximo > num:
        return num
    else:   
        return'O valor que você digitou é invalido!'

numero = max_num()
print(f'{numero}') 

#receber numero inteiro numa faixa min x e max y 

def max_min_num():
    
    minimo = int(input('Por favor digite um numero minimo: ')) 
    maximo = int(input('Por favor digite um numero maximo: ')) 
    num = int(input('Por favor digite um numero: '))
    
    if num > minimo and num < maximo: 
        return num
    else:   
        return'O valor que você digitou é invalido!'

numero = max_min_num()
print(f'{numero}')