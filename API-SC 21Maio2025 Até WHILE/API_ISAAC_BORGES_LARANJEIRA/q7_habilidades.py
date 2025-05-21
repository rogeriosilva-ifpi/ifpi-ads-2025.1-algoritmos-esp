from q1_number_utils import getPositiveInt
import os
def calcularPorcentagem(amostra, todo):
    return (amostra/todo) * 100

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def enterToContinue():
    input('ENTER para continuar ...')
def pesquisa(numAlunos) :
    contador = numAlunos
    numFront = 0
    numBack = 0
    numMobile = 0
    numDados = 0
    clearScreen()
    while contador > 0 :
        print("('x F' -> FrontEnd | 'x B' -> BackEnd | 'x M' -> Mobile | 'x D' -> Dados)")
        alunoEaptidao = input('Insira a quantidade de alunos por aptidão > ')

        numeroPAptidao = int(alunoEaptidao.split()[0])
        tipoAptidao = alunoEaptidao.split()[1]

        if contador - numeroPAptidao < 0 :
            print('Erro! Excedeu o número de entrevistados.')
            enterToContinue()
        elif tipoAptidao != 'F' and tipoAptidao != 'B' and tipoAptidao != 'M' and tipoAptidao != 'D':
            print('Erro! Aptidão inválida.')
            enterToContinue()
        else: 
            if tipoAptidao == 'F' :
                numFront += numeroPAptidao
            elif tipoAptidao == 'B' :
                numBack += numeroPAptidao
            elif tipoAptidao == 'M' :
                numMobile += numeroPAptidao
            else: 
                numDados += numeroPAptidao
            
            contador -= numeroPAptidao
        
        clearScreen()
        
    porcentagemFront = calcularPorcentagem(numFront, numAlunos)
    porcentagemBack = calcularPorcentagem(numBack, numAlunos)
    porcentagemMobile = calcularPorcentagem(numMobile, numAlunos)
    porcentagemDados = calcularPorcentagem(numDados, numAlunos)
    relatorio = f'''
Total: {numAlunos} alunos
Total de Backend: {numBack}
Total de Frontend: {numFront}
Total de Mobile: {numMobile}
Total de Dados: {numDados}
Porcentagem de Backend: {porcentagemBack:.2f} %
Porcentagem de Frontend: {porcentagemFront:.2f} %
Porcentagem de Mobile: {porcentagemMobile:.2f} %
Porcentagem de Dados: {porcentagemDados:.2f} %
'''
    return relatorio


def main() :
    numAlunos = getPositiveInt('Quantos alunos há na sala ? > ')

    relatorio = pesquisa(numAlunos)

    print(relatorio)

main()