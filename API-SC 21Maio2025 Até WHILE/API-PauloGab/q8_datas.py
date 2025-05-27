def main():
    valor_dias1 = data1()
    valor_dias2 = data2()
    
    resultado = calcular_diferenca(valor_dias1, valor_dias2)

    print(resultado)

def data1():
    try:
        print('Digite o ano da primeira data abaixo:')
        ano_data1 = int(input(''))
        print('Digite o mês da primeira data abaixo:')
        mes_data1 = int(input(''))
        print('Digite o dia da primeira data abaixo:')
        dia_data1 = int(input(''))
    
        if ano_data1 < 1 or ano_data1 > 3000:
            print('Ano inválido. Digite os valores novamente!')
            return data1()
        elif mes_data1 < 1 or mes_data1 > 12:
            print('Mês inválido. Digite os valores novamente!')
            return data1()
        elif dia_data1 < 1 or dia_data1 > 30:
            print('Dia inválido. Digite os valores novamente!')
            return data1()
        

        conv_ano = ano_data1 * 365
        conv_mes = mes_data1 * 30

        soma1 = conv_ano + conv_mes + dia_data1

        return soma1
    except ValueError:
        print('Algum valor passado foi inválido. Digite os valores novamente!!')
        return data1()

def data2():
    try:
        print('Digite o ano da segunda data abaixo:')
        ano_data2 = int(input(''))
        print('Digite o mês da segunda data abaixo:')
        mes_data2 = int(input(''))
        print('Digite o dia da segunda data abaixo:')
        dia_data2 = int(input(''))

        if ano_data2 < 1 or ano_data2 > 3000:
            print('Ano inválido. Digite os valores novamente!')
            return data1()
        elif mes_data2 < 1 or mes_data2 > 12:
            print('Mês inválido. Digite os valores novamente!')
            return data1()
        elif dia_data2 < 1 or dia_data2 > 30:
            print('Dia inválido. Digite os valores novamente!')
            return data1()

        conv_ano = ano_data2 * 365
        conv_mes = mes_data2 * 30

        soma2 = conv_ano + conv_mes + dia_data2

        return soma2
    except ValueError:
        print('Algum valor passado foi inválido. Digite os valores novamente!!')
        return data2()


def calcular_diferenca(soma1, soma2):
    diferenca = soma1 - soma2
    if diferenca < 0:
        diferenca_pos = diferenca * (-1)

        conv_ano_dif = diferenca_pos // 365
        conv_mes_dif = (diferenca_pos % 365) // 30
        conv_dia_dif = (diferenca_pos % 365) % 30

        if conv_ano_dif == 0:
            return f'{conv_mes_dif} mês(es) e {conv_dia_dif} dia(s)'
        elif conv_mes_dif == 0:
            return f'{conv_ano_dif} ano(s) e {conv_dia_dif} dia(s)'
        elif conv_dia_dif == 0:
            return f'{conv_ano_dif} ano(s) e {conv_mes_dif} mês(es)'
        elif conv_ano_dif == 0 and conv_mes_dif == 0:
            return f'{conv_dia_dif} dia(s)'
        elif conv_ano_dif == 0 and conv_dia_dif == 0:
            return f'{conv_mes_dif} mês(es)'
        elif conv_mes_dif == 0 and conv_dia_dif == 0:
            return f'{conv_ano_dif} ano(s)'
    elif diferenca > 0:
        diferenca_pos = diferenca * (-1)

        conv_ano_dif = diferenca // 365
        conv_mes_dif = (diferenca % 365) // 30
        conv_dia_dif = (diferenca % 365) % 30

        if conv_ano_dif == 0:
            return f'{conv_mes_dif} mês(es) e {conv_dia_dif} dia(s)'
        elif conv_mes_dif == 0:
            return f'{conv_ano_dif} ano(s) e {conv_dia_dif} dia(s)'
        elif conv_dia_dif == 0:
            return f'{conv_ano_dif} ano(s) e {conv_mes_dif} mês(es)'
        elif conv_ano_dif == 0 and conv_mes_dif == 0:
            return f'{conv_dia_dif} dia(s)'
        elif conv_ano_dif == 0 and conv_dia_dif == 0:
            return f'{conv_mes_dif} mês(es)'
        elif conv_mes_dif == 0 and conv_dia_dif == 0:
            return f'{conv_ano_dif} ano(s)'
        else:
            return f'{conv_ano_dif} ano(s), {conv_mes_dif} mês(es) e {conv_dia_dif} dia(s)'
        
main()

# Ficou boa.. mas tá calculando ligeiramente errado