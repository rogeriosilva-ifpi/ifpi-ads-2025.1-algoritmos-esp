def main():
  print('Viagem com Milhas ou R$')
  origem = input('DE: ')
  destino = input('PARA: ')
  valor_dinheiro = float(input('Valor Passagem (R$): '))
  valor_milhas = int(input('Valor Passagem(Milhas): '))

  valor_padrao = (valor_milhas / 1000) * 70
  valor_baratas = (valor_milhas / 1000) * 14.50

  percentual_padrao = (valor_padrao / valor_dinheiro) * 100
  percentual_baratas = (valor_baratas / valor_dinheiro) * 100

  melhor_forma = calcular_melhor_forma(valor_dinheiro, valor_padrao, valor_baratas)

  resultado = f'''
  Resumo: Comparativo
  Viagem de {origem} para {destino}
  Valor em R$: {valor_dinheiro:.2f}
  Valor em Milhas: {valor_milhas}
  ---------
  Valor Milhas-Padrão (R$ 70/mil): R$ {valor_padrao:.2f}
  \tDiferença: {percentual_padrao:.1f}%
  Valor Milhas-Baratas (R$ 14.50/mil): R$ {valor_baratas:.2f}
  \tDiferença: {percentual_baratas:.1f}%
  ------
  Melhor forma de viajar: {melhor_forma}
  '''

  print(resultado)


def calcular_melhor_forma(valor_dinheiro, valor_padrao, valor_baratas):
  if valor_dinheiro < valor_padrao and valor_dinheiro < valor_baratas:
    return 'Comprar Direto em Reais (R$)'
  elif valor_padrao < valor_dinheiro and valor_padrao < valor_baratas:
    return 'Comprar via Milhas a R$ 70'
  else:
    return 'Comprar via Milhas Baratas a R$ 14,50'


main()