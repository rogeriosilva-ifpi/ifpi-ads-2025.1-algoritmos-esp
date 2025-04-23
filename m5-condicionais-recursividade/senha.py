from pydoc import text
from re import escape


def main():
  senha = input('Senha: ')

  if eh_senha_valida(senha):
    print('Ok. Senha atende aos critérios')
  else:
    print('Senha NÃO atende ao critérios')


def eh_senha_valida(senha):
  if len(senha) >= 8 \
    and contem_letra_maiscula(senha) \
      and contem_letra_minuscula(senha) \
        and contem_numero(senha) \
          and contem_especial(senha):
            return True
  
  return False



def contem_letra_minuscula(senha):
  if len(senha) == 0:
    return False

  if eh_minusculo(senha[0]):
    return True
  
  return contem_letra_minuscula(senha[1:])


def contem_letra_maiscula(senha):
  if len(senha) == 0:
    return False
  
  # return eh_maiusculo(senha[0]) or contem_letra_maiscula(senha[1:])

  if eh_maiusculo(senha[0]):
    return True
  
  return contem_letra_maiscula(senha[1:])


def contem_numero(texto):
  if len(texto) == 0:
    return False

  if eh_numero(texto[0]):
    return True 

  return contem_numero(texto[1:]) 


def contem_especial(texto):
  if len(texto) == 0:
    return False
  
  if eh_especial(texto[0]):
    return True
  
  return contem_especial(texto[1:])


def eh_maiusculo(caracter):
  return ord(caracter) >= 65 and ord(caracter) <= 90


def eh_minusculo(caracter):
  return ord(caracter) >= 97 and ord(caracter) <= 122


def eh_numero(caracter):
  return ord(caracter) >= 48 and ord(caracter) <= 57


def eh_especial(caracter):
  return caracter in '!@#$%ˆ&*()_+'


main()


def obter_temperatura(texto, escala):
  valor = obter_decimal(texto)
  
  if escala == 'K' and valor < 0:
      return obter_temperatura(texto, escala)
  elif escala == 'C' and valor < -273.14:
    return obter_temperatura(texto, escala)
  
  return valor
