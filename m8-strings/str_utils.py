def obter_texto_min(label, tam_minimo):
  valor = input(label)

  while len(valor) < tam_minimo:
    print(f'Por favor digite um nome com pelo menos {tam_minimo} caracter(es)')
    valor = input(label)

  return valor


def obter_texto_max(label, tam_maximo):
  valor = input(label)

  while len(valor) > tam_maximo:
    print(f'Por favor digite um nome com máximo {tam_maximo} caracter(es)')
    valor = input(label)

  return valor


def obter_caracter(label):
  return obter_texto_max(label, 1)


def has_no_e(palavra):
  for letra in palavra:
    if letra == 'e':
      return False
  
  return True