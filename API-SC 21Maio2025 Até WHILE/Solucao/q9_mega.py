from q1_number_utils import  obter_inteiro_minimo, obter_inteiro_positivo


def main():
  premio = float(obter_inteiro_positivo('Prêmio: '))
  imposto = premio * 0.20
  premio_liquido = premio - imposto

  total_contrib = 0
  menor_contrib = None
  maior_contrib = None

  contrib = float(obter_inteiro_minimo('Amigo R$: ', 0))

  while contrib != 0:
    total_contrib += contrib

    if menor_contrib == None or contrib < menor_contrib:
      menor_contrib = contrib

    if maior_contrib == None or contrib > maior_contrib:
      maior_contrib = contrib

    contrib = float(obter_inteiro_minimo('Amigo R$: ', 0))

  # terminou de pedir as contribuicoes
  valor_por_real = premio_liquido / total_contrib

  valor_maior = valor_por_real * maior_contrib
  valor_menor = valor_por_real * menor_contrib

  resultado = f'''
  Prêmio Total: R$ {premio:.2f}
  Impostos: R$ {imposto:.2f}
  Prêmio Líquido: R$ {premio_liquido:.2f}
  ....
  Total Arrecadado: R$ {total_contrib:.2f}
  Maior Contrib: R$ {maior_contrib:.2f}
  Maior Prêmio : R$ {valor_maior:.2f}
  Menor Contrib: R$ {menor_contrib:.2f}
  Menor Prêmio : R$ {valor_menor:.2f}
  '''

  print(resultado)


main()