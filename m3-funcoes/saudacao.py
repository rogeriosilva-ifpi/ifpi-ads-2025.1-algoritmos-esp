def principal():
  cabecalho()
  nome = input('Nome: ')
  print(f'Olá {nome}, é bom ter vc aqui!')
  linha_horinzontal(26, '-')


def linha_horinzontal(tamanho: int, simbolo: str = '_'):
  print(simbolo * tamanho)


def cabecalho():
  linha_horinzontal(25)
  print('>>>> Sys-Saudação <<<<<')
  linha_horinzontal(25)


principal()

