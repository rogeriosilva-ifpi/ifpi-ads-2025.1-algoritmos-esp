from q1_number_utils import obter_inteiro, obter_inteiro_minimo, obter_inteiro_positivo


def main():
  n = obter_inteiro_positivo('N: ')
  m = obter_inteiro_minimo('M: ', n+1)

  while n <= m:
    print(n, primo(n))
    n += 1
    
  print('fim')


def primo(numero):
  if contar_divisores(numero) == 2:
    return 'Primo'

  return ''


def contar_divisores(numero):
  atual = numero
  contador = 0

  while atual > 0:
    if numero % atual == 0:
      contador += 1
    
    atual -= 1
  
  return contador

main()