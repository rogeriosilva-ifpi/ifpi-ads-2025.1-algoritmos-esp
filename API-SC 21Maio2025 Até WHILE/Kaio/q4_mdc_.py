def calcular_mdc(a,b):
    print(f'Calcular mdc {a} e {b}')
    a = abs(a)
    b = abs(b)
    
    while b != 0:
         print(f'{a} = {b} * {b // a} + {a % b}')
         temp = b
         a = temp
         print(f'Mdc {a}')
         return a
         
         
 