def main():
    ...

def entrada_int():
    try:
        num = int(input(''))
        return num
    except ValueError:
        print('Valor inválido. Digite novamente!!')
        return entrada_int()

def sequencia(num):
    qtd = 1
    seq = 0
    teste_seq = 0
    while seq != 0:
        teste_seq = int(input(''))
        if teste_seq == 0:
            return teste_seq
        


        qtd += 1
    


main()