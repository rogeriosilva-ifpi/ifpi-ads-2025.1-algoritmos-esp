from str_utils import contem_proibidas, has_no_e, uses_only, uses_all

def main():
  menu = '''
  >>>> WordPlay <<<
  1 - Listar Todas
  2 - Listar com Tamanho Min N
  3 - Palavras sem Letra "e"
  4 - Palavras sem Letras Proibidas
  5 - Palavras somente com Letras Permitidas
  6 - Palavras com todas as letras obrigatórios

  0 - Sair
  Opcao >>> '''

  opcao = int(input(menu))

  while opcao != 0:
    if opcao == 1:
      mostrar_todos()
    elif opcao == 2:
      mostrar_tamanho_min()
    elif opcao == 3:
      mostrar_sem_letra_e()
    elif opcao == 4:
      mostrar_sem_letras_proibidas()
    elif opcao == 5:
      mostrar_somente_letras_permitidas()
    elif opcao == 6:
      mostrar_com_todas_letras_permitidas()


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


def mostrar_sem_letra_e():
  arquivo = open('br-sem-acentos.txt')
  total = 0
  total_exibidas = 0

  for linha in arquivo:
    total += 1
    palavra = linha.strip()
    if has_no_e(palavra):
      total_exibidas += 1
      print(palavra)
  
  percentual = (total_exibidas / total) * 100
  print(f'Palavras exibidas {total_exibidas}/{total} ({percentual:.3f}%)')

def mostrar_sem_letras_proibidas():
  arquivo = open('br-sem-acentos.txt')
  proibidas = input('Digite as letras proibidas: ')
  total = 0
  total_exibidas = 0

  for linha in arquivo:
    total += 1
    palavra = linha.strip()
    if avoids(palavra, proibidas):
      print(palavra)
      total_exibidas += 1
  
  percentual = (total_exibidas / total) * 100
  print(f'Palavras exibidas {total_exibidas}/{total} ({percentual:.3f}%)')


def avoids(palavra, proibidas):
  return not contem_proibidas(palavra, proibidas)

def mostrar_somente_letras_permitidas():
  arquivo = open('br-sem-acentos.txt')
  total = 0
  total_exibidas = 0

  letras_permitidas = input('Digite as letras permitidas: ')

  for linha in arquivo:
    total += 1
    palavra = linha.strip()
    if uses_only(palavra, letras_permitidas):
      print(palavra)
      total_exibidas += 1

  percentual = (total_exibidas / total) * 100
  print(f'Palavras exibidas {total_exibidas}/{total} ({percentual:.3f}%)')


def mostrar_com_todas_letras_permitidas():
  arquivo = open('br-sem-acentos.txt')
  total = 0
  total_exibidas = 0

  letras_permitidas = input('Digite as letras obrigatórias: ')

  for linha in arquivo:
    total += 1
    palavra = linha.strip()
    if uses_all(palavra, letras_permitidas):
      print(palavra)
      total_exibidas += 1

  percentual = (total_exibidas / total) * 100
  print(f'Palavras exibidas {total_exibidas}/{total} ({percentual:.3f}%)')
main()