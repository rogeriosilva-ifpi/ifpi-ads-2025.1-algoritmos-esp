from q1_number_utils import obter_inteiro_minimo


def main():
  anterior = None

  while True:
    casos = input('Casos: ')
    if casos == 'fim':
      break

    try:
      atual = int(casos)
      if anterior == None:
        anterior = atual
        continue
      else:
        diferenca = atual - anterior
        if diferenca < 0:
          diferenca = diferenca * -1

        percentual = (diferenca / anterior) * 100

        if atual < anterior and percentual >= 15:
          print(f'Em queda {percentual:.1f}%')
        elif atual > anterior and percentual >= 15:
          print(f'Em Alta {percentual:.1f}%')
        else:
          print(f'Em Estabilidade {percentual:.1f}%')

        anterior = atual
    except ValueError :
      print('Valor inválido')


main()