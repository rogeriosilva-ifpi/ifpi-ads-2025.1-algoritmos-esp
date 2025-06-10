from q1_number_utils import obter_inteiro_positivo


def main():
  qtd = obter_inteiro_positivo('Registros: ')
  count_b = 0
  count_f = 0
  count_d = 0
  count_m = 0

  while qtd > 0:
    valor = input('R: ')
    numero = int(valor.split()[0])
    tipo = valor.split()[1]

    if tipo == 'B':
      count_b = count_b + numero
    elif tipo == 'F':
      count_f = count_f + numero
    elif tipo == 'M':
      count_m = count_m + numero
    elif tipo == 'D':
      count_d = count_d + numero
    else:
      ...

    qtd -= 1

  total = count_b + count_d + count_f + count_m

  if total > 0:
    perc_b = count_b / total * 100
    perc_f = count_f / total * 100
    perc_m = count_m / total * 100
    perc_d = count_d / total * 100

    resultado = f'''
    Total: {total} alunos
    Total de Backend: {count_b}
    Total de Frontend: {count_f}
    Total de Mobile: {count_m}
    Total de Dados: {count_d}
    Percentual de Backend: {perc_b:.2f} %
    Percentual de Frontend: {perc_f:.2f} %
    Percentual de Mobile: {perc_m:.2f} %
    Percentual de Dados: {perc_d:.2f} %
    '''

    print(resultado)

  print('Fim')


main()