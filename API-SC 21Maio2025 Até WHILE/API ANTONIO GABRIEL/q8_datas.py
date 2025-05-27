while True:
    
    dia_1 = int(input('Digite o  dia(1 a 30): '))
    if dia_1 >= 1 and dia_1 <= 30:
        break
    print('Dia inválida, digite novamente')
        


while True:
        
    mes_1 = int(input('Digite o  mês(1 a 12): '))
    if mes_1 >=1 and mes_1 <=12:
        break
    print('Mês invalido, digite novamente')

while True:

    ano_1 = int(input('Digite o  ano(1 a 3000): '))
    if ano_1 >=1 and ano_1 <=3000:
        break
    print('Ano inválido, digite novamente')
print('--------------------------------------------')

while True:
    
    dia_2 = int(input('Digite o  dia(1 a 30): '))
    if dia_2 >= 1 and dia_2 <= 30:
        break
    print('Dia inválida, digite novamente')
        


while True:
        
    mes_2 = int(input('Digite o  mês(1 a 12): '))
    if mes_2 >=1 and mes_2 <=12:
        break
    print('Mês invalido, digite novamente')

while True:

    ano_2 = int(input('Digite o  ano(1 a 3000): '))
    if ano_2 >=1 and ano_2 <=3000:
        break
    print('Ano inválido, digite novamente')



if ano_1 > ano_2:
        distancia_ano = ano_1 - ano_2
else:
    distancia_ano = ano_2 - ano_1

if mes_1 > mes_2:
    distancia_meses = mes_1 - mes_2
else:
    distancia_meses = mes_2 - mes_1

if dia_1 > dia_2:
    distancia_dia = dia_1 - dia_2
else:
    distancia_dia = dia_2 - dia_1


    


print(f'A distancia das datas {dia_1}/{mes_1}/{ano_1} e {dia_2}/{mes_2}/{ano_2} é de {distancia_ano} ano(s) {distancia_meses} meses e {distancia_dia} dia(s)')


# ficou bem estranho esses vários while True.. 
# Sem funcoes.
# Logica Não bate.