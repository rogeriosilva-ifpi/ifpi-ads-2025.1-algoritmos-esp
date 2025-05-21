import os
from q1_number_utils import getIntInRange, getPositiveInt

def menu_inicial(num):
    if num == 1 :
        print('''
    ___________________________________________________________
                            COMANDA    
                               
            1 - INSERIR PRODUTO
            2 - CALCULAR CONTA
            3 - IMPRIMIR CONTA
            4 - CONFIRMAR PAGAMENTO
            
    ___________________________________________________________
        ''')


def getTaxa(valorTotal, C) :
    if C <= 10 and valorTotal <= 200 :
        return (valorTotal * 100 / 110) * 0.1
    else: 
        return 0

def gerarConta(valorTotal, C, pagantes) :
    taxa = getTaxa(valorTotal, C)
    porPessoa = valorTotal / pagantes  
    parcial = valorTotal - taxa 
    
    
    print(f'''
    ___________________________________________________________
                             CONTA        
                               
            VALOR TOTAL PROVISORIO : R$ {parcial:.2f}
            VALOR POR PESSOA       : R$ {porPessoa:.2f}
            VALOR TAXA DE SERVIÇO  : R$ {taxa:.2f}
            VALOR TOTAL COM TAXA   : R$ {valorTotal:.2f}

    ___________________________________________________________
''')



def clearScreen():
    os.system('cls' if os.system == 'nt' else 'clear')

def calcularPreco(A, C, TG) :
    precoTotal = (A * 5) + (C * 9) + (TG * 39)

    if C <= 10 and precoTotal <= 200 :
        precoTotal += 0.1 * precoTotal

    return precoTotal

def enterToContinue():
    input('ENTER para continuar ... ')

def main() :
    opcao = 0
    numCervejas = 0
    numAguas = 0
    numTiraGosto = 0
    precototal = 0

    while opcao != 4 :
        clearScreen()
        menu_inicial(1)
        opcao = getIntInRange(' > ', 1, 4)
        if opcao == 1 :
            print("('x C' -> Cerveja | 'x A' -> Água | 'x TG' -> Tira-gosto)")
            produto = input('Insira a quantidade e o produto > ')

            numProduto = int(produto.split()[0])
            tipoProduto = produto.split()[1]

            if tipoProduto == 'C' :
                numCervejas += numProduto
            elif tipoProduto == 'A' :
                numAguas += numProduto
            elif tipoProduto == 'TG' :
                numTiraGosto += numProduto

        elif opcao == 2 :
            precototal = calcularPreco(numAguas, numCervejas, numTiraGosto)
            clearScreen()
            print('Conta calculada!')
            enterToContinue()

        elif opcao == 3 :
            if precototal > 0 : 
                pessoasPagantes = getPositiveInt('Quantas pessoas irão pagar? > ')
                clearScreen()
                gerarConta(precototal, numCervejas, pessoasPagantes)
                enterToContinue()
            else:
                clearScreen()
                print('INSIRA UM PRODUTO!')
                enterToContinue()

    clearScreen()            
    print('FIM!')



        

main()