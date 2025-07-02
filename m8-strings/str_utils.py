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

def contem_proibidas(palavra, proibidas):
  for caracter in proibidas:
    if contem_caracter(palavra, caracter):
      return True
  
  return False

def contem_caracter(palavra, caracter):
  for letra in palavra:
    if letra == caracter:
      return True
  
  return False

def uses_only(palavra, letras_permitidas):
  # usa somente as permitidas
  for caracter in palavra:
    if not contem_caracter(letras_permitidas, caracter):
      return False
  
  return True

def uses_all(palavra, letras_obrigatorias):
  for letra in letras_obrigatorias:
    if not contem_caracter(palavra, letra):
      return False
  return True

  