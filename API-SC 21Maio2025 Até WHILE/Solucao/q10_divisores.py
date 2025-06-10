from q1_number_utils import obter_inteiro, obter_inteiro_minimo, obter_inteiro_positivo


def main():
  a = obter_inteiro_positivo('N: ')
  b = obter_inteiro_minimo('M: ', a+11)

  while a <= b:
    print(a, '(', contar_divisores(a), ')')
    a += 1
    
  print('fim')


def contar_divisores(numero):
  atual = numero
  contador = 0

  while atual > 0:
    if numero % atual == 0:
      contador += 1
    
    atual -= 1
  
  return contador

main()