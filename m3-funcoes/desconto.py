from utilidades import calcular_percentual

def principal():
  valor_compra = float(input('Compra R$: '))
  perc_desconto = float(input('Desconto (%): '))
  qtd_parcelas = int(input('Qtd Parcelas: '))

  valor_desconto = calcular_percentual(valor_compra, perc_desconto)
  valor_final = valor_compra - valor_desconto
  valor_parcela = valor_final / qtd_parcelas

  resultado = f'''
    Valor Compra  : R$ {valor_compra:.2f}
    Valor Desconto: -R$ {valor_desconto:.2f} ({perc_desconto}%)
    Valor a Pagar : R$ {valor_final:.2f}
    Parcelamento  : {qtd_parcelas}x R$ {valor_parcela:.2f}
  '''
  print(resultado)


principal()