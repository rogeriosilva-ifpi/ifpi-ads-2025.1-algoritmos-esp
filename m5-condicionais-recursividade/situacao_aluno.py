def main():
  nota1 = obter_numero_decimal_faixa('Nota 1: ', 0, 10)
  nota2 = obter_numero_decimal_faixa('Nota 2: ', 0, 10)
  nota3 = obter_numero_decimal_faixa('Nota 3: ', 0, 10)

  media = computar_media(nota1, nota2, nota3)

  situacao_aluno = computar_situacao(media)

  print(f'Sua Média foi {media:.2f}')
  print(f'Sua situação é {situacao_aluno}')


# funcionalidades
def computar_media(n1, n2, n3):
  return (n1 + n2 + n3) / 3


def computar_situacao(media):
  if media >= 7:
    if media == 10:
      return 'APROVADO - com Louvor'
    else:
      return 'APROVADO'
  elif media >= 4:
    return 'PROVA FINAL'
  elif media >= 2.5:
    return 'REPROVADO - Direto'
  else:
    return 'JUBILAMENTO'


# Utilidades
def obter_numero_decimal(texto):
  entrada = input(texto)
  try:
    numero = float(entrada)
    return numero
  except ValueError:
    print(f'Error: o valor "{entrada}" não é válido')
    return obter_numero_decimal(texto)
  

def obter_numero_decimal_faixa(texto, minimo, maximo):
  numero = obter_numero_decimal(texto)

  if numero < minimo or numero > maximo:
    print(f'O valor {numero} está fora da faixa[{minimo}, {maximo}]')
    return obter_numero_decimal_faixa(texto, minimo, maximo)
  
  return numero


main()