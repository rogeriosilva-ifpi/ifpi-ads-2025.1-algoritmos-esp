def main():
  menu = '''
  >>>> WordPlay <<<
  1 - Listar Todas
  2 - Listas com Tamanho Min N

  0 - Sair
  Opcao >>> '''

  opcao = int(input(menu))

  while opcao != 0:
    # lido com a opcao escolhi
    if opcao == 1:
      mostrar_todos()
    elif opcao == 2:
      mostrar_tamanho_min()

    input('Enter to continue...')
    opcao = int(input(menu))


def mostrar_todos():
  arquivo = open('br-sem-acentos.txt')
  contador = 0
  for linha in arquivo:
    contador += 1
    palavra = linha.strip()
    print(palavra)

  print('Total de Palavras:', contador)


def mostrar_tamanho_min():
  tamanho = int(input('Tamanho Mínimo: '))

  arquivo = open('br-sem-acentos.txt')
  total = 0
  total_exibidas = 0

  for linha in arquivo:
    palavra = linha.strip()
    total += 1
    if len(palavra) >= tamanho:
      total_exibidas += 1
      print(palavra)

  percentual = (total_exibidas / total) * 100

  print(f'Palavras exibidas {total_exibidas}/{total} ({percentual:.3f}%)')

main()