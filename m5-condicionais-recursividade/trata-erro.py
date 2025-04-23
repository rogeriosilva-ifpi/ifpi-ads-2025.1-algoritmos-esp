def main():
  
  print('Início')

  numero = obter_inteiro_positivo('Número 1: ')
  numero2 = obter_inteiro_positivo('Número 2: ')

  try:
    r = numero / numero2
    print(f'Resultado {numero}/{numero2} = {r}')
  except ZeroDivisionError:
    print('Não é possível divisão por Zero!')
  except:
    print('Erro desconhecido!')


  print('Fim!')


def obter_inteiro(texto):
  n = input(texto)
  
  try:
    return int(n)
  except:
    print(f'"{n}" inválido! Favor tente novamente!')
    m = obter_inteiro(texto)
    return m
  
def obter_inteiro_positivo(texto):
  numero = obter_inteiro(texto)

  if numero > 0:
    return numero
  
  print(f'O número "{numero}" não é positivo!')
  return obter_inteiro_positivo(texto)


def obter_inteiro_negativo(texto):
  numero = obter_inteiroI(texto):

  if numero < 0:
    return numero
  
  return obter_inteiro_negativo(texto)
    
  

main()