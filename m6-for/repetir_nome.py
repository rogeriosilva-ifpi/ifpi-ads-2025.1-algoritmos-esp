def main():
  nome = input('Qual seu nome? ')
  qtd = int(input('Quantas vezes? '))

  # for i in [1,2,3,4,5,6,7]:
  for i in range(0, qtd, 1):
    print(f'{i} > {nome}')


main()