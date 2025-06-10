def main():
  n = obter_inteiro_positivo('N: ')
  m = obter_inteiro_minimo('M: ', n + 1)

  for numero in range(n, m + 1, 1):
    qtd_divisores = contar_divisores(numero)
    # operador ternário de python
    eh_primo = 'PRIMO' if qtd_divisores == 2 else ''
    print(f'{numero} -> ({qtd_divisores}) {eh_primo}')


def contar_divisores(numero):
  contador = 0

  for d in range(1, numero + 1, 1):
    if numero % d == 0:
      contador += 1
  
  return contador


def obter_inteiro(label):
  entrada = input(label)

  try:
    numero = int(entrada)
    return numero
  except:
    print('Valor inválido!')
    return obter_inteiro(label)

def obter_inteiro_positivo(label):
  numero = obter_inteiro(label)

  while numero <= 0:
    print('Valor zero ou negativo!')
    numero = obter_inteiro(label)
  
  return numero


def obter_inteiro_minimo(label, minimo):
  numero = obter_inteiro(label)

  while numero < minimo:
    print(f'O número deve ser no mínimo "{minimo}"')
    numero = obter_inteiro(label)

  return numero



main()