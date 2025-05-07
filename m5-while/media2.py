def main():
  somatorio = 0
  contador = 0

  while True:
    numero = int(input())
    # fail fast
    if numero < 0:
      break
    
    somatorio += numero
    contador += 1

  if contador > 0:
    media = somatorio / contador
    print('Média -->', media)
  else:
    print('Nenhum número computado.')

main()
