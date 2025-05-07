def main():
  nome = input('Nome: ')
  vezes = int(input('Vezes: '))

  escrever(nome, vezes)

  print('Fim!')


def escrever(nome, vezes):
  if vezes == 0:
    return
  
  print(vezes, nome)
  escrever(nome, vezes - 1)

main()