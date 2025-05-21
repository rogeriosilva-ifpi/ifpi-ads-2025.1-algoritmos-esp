def main():
    data_1_ano = data_1_a()
    data_1_mes = data_1_m()
    data_1_dia = data_1_d()
    data_2_ano = data_2_a()
    data_2_mes = data_2_m()
    data_2_dia = data_2_d()
    distancia(data_1_ano, data_1_mes, data_1_dia , data_2_ano, data_2_mes, data_2_dia)
    
    
def data_1_a():
    while True:
        entrada = input('Digite o ano da data 1  :')
        try:
            num = int(entrada)
            max = int(3000)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do ano é inválido, digite outro!!!')
                return data_1_a()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_1_a()
        
        
def data_2_a():
    while True:
        entrada = input('Digite o ano da data 2  :')
        try:
            num = int(entrada)
            max = int(3000)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do ano é inválido, digite outro!!!')
                return data_2_a()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_2_a()
        
        
def data_1_m():
    while True:
        entrada = input('Digite o mes da data 1  :')
        try:
            num = int(entrada)
            max = int(12)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do mes é inválido, digite outro!!!')
                return data_1_m()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_1_m()
        
        
def data_2_m():
    while True:
        entrada = input('Digite o mes da data 2  :')
        try:
            num = int(entrada)
            max = int(12)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do mes é inválido, digite outro!!!')
                return data_2_m()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_2_m()
        
        
def data_2_d():
    while True:
        entrada = input('Digite o dia da data 2  :')
        try:
            num = int(entrada)
            max = int(30)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do mes é inválido, digite outro!!!')
                return data_2_d()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_2_d()
        
        
def data_1_d():
    while True:
        entrada = input('Digite o dia da data 1  :')
        try:
            num = int(entrada)
            max = int(30)
            min = int(1)
            if (num > max) and (num < min):
                print('Valor do mes é inválido, digite outro!!!')
                return data_1_d()
            else:
                return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return data_1_d()
        
        
def distancia(data_1_ano, data_1_mes, data_1_dia , data_2_ano, data_2_mes, data_2_dia):
    total_dias_1 = (data_1_ano * 365) + (data_1_mes * 30) + data_1_dia
    total_dias_2 = (data_2_ano * 365) + (data_2_mes * 30) + data_2_dia
    diferença = total_dias_1 - total_dias_2
    if diferença < 0:
        return diferença * -1
    ano = diferença // 365
    resto_ano = diferença % 365
    mes = resto_ano // 30
    resto_mes = resto_ano % 30
    dia = resto_mes
    if ano > 0 and dia < 0  and mes < 0:
        print(f'{ano} anos.')
    if mes > 0 and dia < 0 and ano < 0:
        print(f'{mes} meses.')
    if dia > 0 and mes < 0 and ano < 0:
        print(f'{dia} dias')
    if ano > 0 and dia > 0  and mes < 0:
        print(f'{ano} anos e {dia} dias')
    if ano > 0 and dia < 0  and mes > 0:
        print(f'{ano} anos e {mes} meses')
    if ano < 0 and dia > 0  and mes > 0:
        print(f'{mes} meses e {dia} dias')
    else:
        print(f'{ano} anos e {mes} meses e {dia} dias')
        
main()