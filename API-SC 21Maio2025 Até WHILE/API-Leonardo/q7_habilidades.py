def main():
    total_alunos = 0
    total_f = 0
    total_m = 0
    total_b = 0
    total_d = 0
    while True:
        entrada = int(input('Digite quantas entradas deseja: '))
        while entrada > 0:
            pedido = input('Digite o curso e a quantidade de alunos nele : ')
            n = int(pedido.split()[0])
            tipo = pedido.split()[1]
            total_alunos += n
            if tipo == 'F':
                total_f += n
            if tipo == 'M':
                total_m += n
            if tipo == 'B':
                total_b += n
            if tipo == 'd':
                total_d += n
            entrada -= 1
        break
    if total_alunos:
        percentual_b = (total_b / total_alunos) * 100
        percentual_f = (total_b / total_alunos) * 100
        percentual_m = (total_b / total_alunos) * 100
        percentual_d = (total_b / total_alunos) * 100
    print(f'Total : {total_alunos} alunos')
    print(f'Total de Backend : {total_b} alunos')
    print(f'Total de Frontend : {total_f} alunos')
    print(f'Total de Mobile : {total_m} alunos')
    print(f'Total de Dados : {total_d} alunos')
    print(f'Percentual de backend: {percentual_b:.2f}')
    print(f'Percentual de Frontend: {percentual_f:.2f}')
    print(f'Percentual de Mobile: {percentual_m:.2f}')
    print(f'Percentual de Dados: {percentual_d:.2f}')
main()