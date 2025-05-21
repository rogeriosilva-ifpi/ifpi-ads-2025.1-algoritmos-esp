import os

def main():
    somatorio = 0
    contador = 0

    while True:
      opcao = int(input('Digite uma opção: '))
    
    if opcao == END:
      

    elif opcao == ADD_PRODUTO:
      menu_produtos()






def show_menu():
 menu = '''
 ======>MENU<======
 1 - Inserir produto
 2 - Calcular conta
 3 - Imprimir conta
 '''
 print(show_menu)

def menu_produtos():
  menu = '''
  1 - Cerveja
  2 - Tira-gosto
  3 - Água
  '''
  print(menu_produtos)

# def produtos():

#  def clear_screen():
# os.system('clear')


#constants
ADD_PRODUTO = 1
END = 0

main()