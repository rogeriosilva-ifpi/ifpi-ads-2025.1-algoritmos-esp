def main():
    d = int(input('Digite o dia do seu nascimento: '))
    m = int(input('Digite o mes do seu nascimento: '))
    a = int(input('Digite o ano do seu nascimento: '))
    d2= int(input('Digite o dia do seu nascimento: '))
    m2 = int(input('Digite o mes do seu nascimento: '))
    a2 =  int(input('Digite o ano do seu nascimento: '))
    dif_dias = abs(d - d2)
    dif_m = abs(m - m2)
    dif_ano = abs(a-a2)
    resultado = print('A diferença entre dias é de {},  {} meses, e d {} anos'.format(dif_dias,dif_m,dif_ano))

main()


# abs nao permitod. Mas tudo bem. 
# Lógica assim não funcoinar.. se for 31/12/2024 para 01/01/2025 deveria ser 1 dia de distancia