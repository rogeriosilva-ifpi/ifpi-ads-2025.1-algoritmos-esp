
def main():
    pedir_dia1 = pedir_dia()
    
    
    
    '''diavalido1 = verificar_dia(dia1)
    mes1 = int(input("Digite o mês"))
    ano1 = int(input("Digite o ano:"))'''

    print("Data 2: ")
    dia2 = int(input("Digite o dia: "))
    mes2 = int(input("Digite o mês"))
    ano2 = int(input("Digite o ano:"))


    #Processamento
    '''diavalido1 = verificar_dia(dia1)
    diavalido2 = verificar_dia(dia2)
    mesvalido1 = verificar_mes(mes1)
    mesvalido2 = verificar_mes(mes2)
    anovalido1 = verificar_ano(ano1)
    anovalido2 = verificar_ano(ano2)'''



def pedir_dia():
    dia = int(input("Digite o dia:"))
    dia = int(input("Digite o dia: "))
    while (dia < 1 and dia > 30):
        dia = int(input("Digite novamente o dia: "))
        return dia

def pedir_mes(mes):
    while (mes < 1 and mes > 30):
        mes = int(input("Digite novamente o mês: "))
        return mes
    
def pedir_ano(ano):
    while (ano < 1 and ano > 3000):
        ano = int(input("Digite novamente o ano:"))
        return ano




main()
