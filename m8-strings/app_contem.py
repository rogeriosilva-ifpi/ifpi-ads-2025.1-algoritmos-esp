from str_utils import obter_texto_min, obter_caracter

def main():
  nome = obter_texto_min('Nome: ', 3)
  char = obter_caracter('Digite uma letra: ')

  if contem_caracter_while(nome, char):
    print(f'O nome {nome} contém o caratere "{char}"')
  else:
    print(f'O nome {nome} NÃO contém o caratere "{char}"')


def contem_caracter(nome, char):
  for letra in nome:
    if letra == char:
      return True

  return False

def contem_caracter_while(nome, char):
  i = 0
  while i < len(nome):
    letra = nome[i]
    if letra == char:
      return True
    
    i += 1

  return False

main()