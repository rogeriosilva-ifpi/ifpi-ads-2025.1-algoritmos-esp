dia = int(input('Digite o dia do nascimento: '))
mes = str(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

#processamento
days = dia / 365
resto =  dia % days

month = 12 - mes
ano_div = 2025 - ano

print()