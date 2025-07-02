import os
from map_filter_reduce import mapear, filtrar, reduzir


def main():
  os.system('clear')
  nomes = load_nomes()

  menu = f'''
  >>> Brincadeira de Nomes - ({len(nomes)})<<<
  1 - Add Nome
  2 - List Nomes
  3 - List Nomes tamanho Ímpar (filter)
  4 - List somente vogais dos nomes (map)
  5 - Contar total de caracteres (reduce)
  6 - Contar ocorrências de caractere (reduce)
  7 - Listar somente com dado caractere (filter)
  8 - List Nomes com tamanhos (map)


  0 - Encerrar
  >>> '''

  opcao = int(input(menu))

  while opcao != 0:
    if opcao == 1:
      nome = input('Nome: ')
      nomes.append(nome)
      print('Nome adicionado com sucesso!')
    elif opcao == 2:
      show_nomes(nomes)
    elif opcao == 3:
      nomes_filtrados = filtrar(nomes, eh_tamanho_impar)
      show_nomes(mapear(nomes_filtrados, nomes_com_tamanho))
    elif opcao == 4:
      nomes_transformados = mapear(nomes, somente_vogais)
      show_nomes(nomes_transformados)
    elif opcao == 5:
      total = reduzir(nomes, contar_caracteres_redutora, 0)
      print(f'O total de letras é {total}')
    elif opcao == 6:
      caracter = input('Qual caractere? ')
      f = lambda acc,item:acc+contar_caractere_nome(item, caracter)
      total = reduzir(nomes, f, 0)
      print(f'Temos {total} ocorrências do caractere "{caracter}"')
    elif opcao == 7:
      caracter = input('Qual caractere? ')
      nomes_filtrados = filtrar(nomes, lambda item:contem_caractere(item, caracter))
      show_nomes(nomes_filtrados)
    elif opcao == 8:
      nomes_transformados = mapear(nomes, nomes_com_tamanho)
      show_nomes(nomes_transformados)

    input('Enter >>> ')
    os.system('clear')

    opcao = int(input(menu))


# Funcoes Auxiliares MFR
def eh_tamanho_impar(nome):
  return len(nome) % 2 != 0

def somente_vogais(nome):
  novo_nome = ''
  for letra in nome:
    if eh_vogal(letra):
      novo_nome += letra
  
  return novo_nome


def contar_caractere_nome(nome, caracter):
  total = 0
  for letra in nome:
    if letra == caracter:
      total += 1
  
  return total


def contar_caracteres_redutora(acumulado, item):
  return acumulado + len(item)


def nomes_com_tamanho(nome):
  return f'{nome} - ({len(nome)})'

def contem_caractere(nome, caractere):
  for letra in nome:
    if letra == caractere:
      return True
  
  return False


def eh_vogal(letra):
  vogais = 'aáàãâeéêiíoóõôuúAÁÀÃÂEÉÊIÍOÓÕÔUÚ'
  for vogal in vogais:
    if letra == vogal:
      return True
  
  return False


def show_nomes(nomes):
  print(f'Temos {len(nomes)} nomes cadastrados: ')

  for nome in nomes:
    print(nome)

  print(15 * '-')


def load_nomes():
  lista = []
  arquivo = open('nomes.txt')
  for linha in arquivo:
    lista.append(linha.strip())

  return lista


main()