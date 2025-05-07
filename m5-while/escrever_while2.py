def main():
  nome = input('Nome: ')
  vezes = int(input('Vezes: '))
  total = vezes

  while vezes > 0:
    print(f'{vezes}/{total}', nome)
    vezes = vezes - 1

  print('Fim.')


main()