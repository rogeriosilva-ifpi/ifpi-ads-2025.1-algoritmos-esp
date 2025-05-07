def main():
  somatorio = 0
  contador = 0

  while True:
    numero = int(input())
    # fail fast
    if numero == 0:
      break

    if numero < 0:
      continue
    
    somatorio += numero
    contador += 1

  if contador > 0:
    media = somatorio / contador
    resultado = f'''
    Números  : {contador}
    Somatório: {somatorio}
    Média    : {media:.2f}
    '''
    print(resultado)
  else:
    print('Nenhum número computado.')

main()
