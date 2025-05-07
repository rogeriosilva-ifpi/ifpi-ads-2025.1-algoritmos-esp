def main():
  nome = input('Nome: ')
  vezes = int(input('Vezes: '))
  contador = 0

  while contador < vezes:
    print(contador, nome)
    contador = contador + 1

  print('Fim.')


main()