def main():
    total_casos = 0
    dias = 0
    while True:
        qntd_casos = input('Casos: ')
        if qntd_casos == 'fim':
            break
        try:
            entrada = int(qntd_casos)
            total_casos += entrada
            dias += 1
            print(f'No dia {dias} teve um total de : {qntd_casos}')
            return qntd_casos
        except ValueError:
            print('Valor não computado!!!')
            return 0
    media = total_casos / dias
    print(f'O total de casos é : {total_casos}')
    print(f'A média de casos por dia é : {media}')
    
main()

# O returno 0 na main invalida a questão. 