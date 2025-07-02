import os

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
  6 - Contar ocorrênciar caractere (reduce)
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
      nomes_filtrados = filtrar_tam_impar(nomes)
      show_nomes(nomes_filtrados)
    elif opcao == 4:
      nomes_transformados = mapear_em_vogais(nomes)
      show_nomes(nomes_transformados)
    elif opcao == 5:
      total = contar_total_caracteres(nomes)
      print(f'O total de letras é {total}')
    elif opcao == 6:
      caracter = input('Qual caractere? ')
      total = contar_caractere_lista(nomes, caracter)
      print(f'Temos {total} ocorrências do caractere "{caracter}"')
    elif opcao == 7:
      caracter = input('Qual caractere? ')
      nomes_filtrados = filtrar_por_contem_caractere(nomes, caracter)
      show_nomes(nomes_filtrados)
    elif opcao == 8:
      nomes_transformados = mapear_incluir_tamanho(nomes)
      show_nomes(nomes_transformados)

    input('Enter >>> ')
    os.system('clear')

    opcao = int(input(menu))


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


# Features
def filtrar_por_contem_caractere(nomes, caracter):
  cesta = []
  for nome in nomes:
    if contem_caractere(nome, caracter):
      cesta.append(nome)
  
  return cesta


def contem_caractere(nome, caracter):
  for letra in nome:
    if letra == caracter:
      return True
  
  return False


def contar_caractere_lista(nomes, caracter):
  acumulado = 0
  for nome in nomes:
      quantidade = contar_caractere_nome(nome, caracter)
      acumulado = acumulado + quantidade
  
  return acumulado


def contar_caractere_nome(nome, caracter):
  total = 0
  for letra in nome:
    if letra == caracter:
      total += 1
  
  return total

def contar_total_caracteres(nomes):
  acumulado = 0
  for nome in nomes:
    acumulado = acumulado + len(nome)
  
  return acumulado


def filtrar_tam_impar(nomes):
  cesta = []
  for nome in nomes:
    if len(nome) % 2 != 0:
      cesta.append(nome)
  
  return cesta

def mapear_incluir_tamanho(nomes):
  cesta = []
  for nome in nomes:
    nome_transformado = nome + ' - ' + str(len(nome))
    cesta.append(nome_transformado)
  
  return cesta


def mapear_em_vogais(nomes):
  cesta = []
  for nome in nomes:
    nome_transformado = somente_vogais(nome)
    cesta.append(nome_transformado)
  
  return cesta


def somente_vogais(nome):
  novo_nome = ''
  for letra in nome:
    if eh_vogal(letra):
      novo_nome += letra
  
  return novo_nome

def eh_vogal(letra):
  vogais = 'aáàãâeéêiíoóõôuúAÁÀÃÂEÉÊIÍOÓÕÔUÚ'
  for vogal in vogais:
    if letra == vogal:
      return True
  
  return False

main()