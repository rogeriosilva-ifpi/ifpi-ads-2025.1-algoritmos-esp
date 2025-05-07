import os


def main():
  clear_screen()
  # Variáveis
  somatorio = 0
  contador = 0
  
  while True:
    show_menu()
    opcao = int(input('Digite sua opção >>> '))
    
    if opcao == SAIR:
      clear_screen()
      break
    elif opcao == NEW_NUMBER:
      somatorio = somatorio + int(input('Número: '))
      contador += 1
    elif opcao == SUM:
      print(f'A Soma dos Números é {somatorio}')
    elif opcao == AVERAGE:
      media = somatorio / contador
      print(f'A Média é {media:.2f}')
    elif opcao == COUNT:
      print(f'Já foram digitados {contador} números')
    else:
      print('Opção Inválida!')
      enter_to_continue()
      continue
    
    
    print('Operação realizada com sucesso!')
    enter_to_continue()
    

def show_menu():
  menu = '''
  ========== NUMBERS ===========
  1 - Adicionar Novo Número
  2 - Somatório dos Números
  3 - Quantos Números foram digitados
  4 - Média dos Números
  ...
  0 - Encerrar
  '''
  print(menu)


def clear_screen():
  os.system('clear')


def enter_to_continue():
  input('<Enter> to continue...')
  clear_screen()


# CONSTANTS
SAIR = 0
NEW_NUMBER = 1
SUM = 2
COUNT = 3
AVERAGE = 4

main()
