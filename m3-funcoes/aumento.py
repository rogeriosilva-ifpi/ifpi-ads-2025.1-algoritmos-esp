from utilidades import calcular_percentual


def principal():
  salario = float(input('Salário: '))
  percentual = float(input('Reajuste (%): '))

  valor_reajuste = calcular_percentual(salario, percentual)
  novo_salario = salario + valor_reajuste

  print(f'Seu Salário era R$ {salario:.2f}')
  print(f'Sofreu um reajuste de {valor_reajuste:.2f} ({percentual}%)')
  print(f'Seu Novo Salário agora é R$ {novo_salario:.2f}')


principal()