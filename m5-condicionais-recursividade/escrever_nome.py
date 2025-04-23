def main():
  quantidade = int(input('Quantidade: '))
  nome = input('Nome: ')

  repetir_nome(nome, quantidade)

  print('Fim!')


def repetir_nome(nome, quantidade):
  if quantidade == 0:
    return
  
  print(nome)
  repetir_nome(nome, quantidade - 1)



main()