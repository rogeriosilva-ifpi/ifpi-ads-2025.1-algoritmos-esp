def main():
    a = int(input('A: '))
    b = int(input('B: '))

    eh_positivo = valida_posivito(a, b)

    print(eh_positivo)

def valida_posivito(a, b):
    if a > 0:
        return a
    
    else: 
        print('Esse número não é posivito.')

main()