from utils import continuar, limpar_tela
from ulid import ULID
import json

def main():
  limpar_tela()
  
  series = carregar_arquivo('series.txt')

  menu = '''
  >>>> Séries Fantásticas <<<<
  1 - Add
  2 - List
  3 - List by Year
  4 - Listar nome e Tempo de Lançamento
  5 - Listar Séries Ativas (ainda lançando episódios)
  6 - Pesquisar Parte do Nome
  7 - Listar Ordenado por ano de Lançamento(decrecente)
  8 - Pesquisar por Nome de Ator/Atriz
  9 - Pesquisa por Gênero
  10 - Contar por Gênero
  11 - Listar por Avaliação Min-Max

  0 - Sair
  Opcão >>> '''

  opcao = int(input(menu))

  while opcao != 0:

    if opcao == 1:
      nova_serie = obter_nova_serie()
      series.append(nova_serie)
    elif opcao == 2:
      listar_series(series)
    elif opcao == 3:
      inicio, fim = map(int, input('Ano Início-Fim: ').split('-'))  #'2005-2010'
      series_filtradas = filtrar_por_periodo(series, inicio, fim)
      listar_series(series_filtradas)
    elif opcao == 4:
      lista = list(map(formatar_ha_x_anos, series))
      for item in lista:
        print(item)

    continuar()
    limpar_tela()
    opcao = int(input(menu))

  # encerrando
  salvar_em_arquivo(series, 'series.txt')

# Funcionalidades
def carregar_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo)
  conteudo = arquivo.read()

  if len(conteudo) > 0:
    series = json.loads(conteudo)
  else:
    series = []

  print(f' {len(series)} séries carregadas com sucesso!')
  return series


def salvar_em_arquivo(series, nome_arquivo):
  arquivo = open(nome_arquivo, 'w')
  conteudo = json.dumps(series)
  arquivo.write(conteudo)

  arquivo.close()
  print(f' {len(series)} séries salvas com sucesso!')


def formatar_ha_x_anos(serie):
  anos = 2025 - serie['ano']
  resultado = f'{serie['nome']}, lançada há {anos} anos.'

  return resultado

def obter_nova_serie():
  serie = {'id':str(ULID())}
  serie['nome'] = input('Nome: ')
  serie['ano'] = int(input('Ano de Lançamento: '))
  serie['genero'] = input('Genero: ')
  serie['avaliacao'] = float(input('Avalição[0.0 a 5.0]: '))

  return serie


def listar_series(series:list[dict]):
  print(f'Listando {len(series)} séries:')

  for serie in series:
    resultado = f'{serie['id']} > {serie['nome']} ({serie['ano']}) - G: {serie['genero']} - Nota: {serie['avaliacao']:.1f}'
    print(resultado)

  print('>>>>>>>> Fim <<<<<<<<<')


def filtrar_por_periodo(series, inicio, fim):
  cesta = []

  for serie in series:
    if serie['ano'] >= inicio and serie['ano'] <= fim:
      cesta.append(serie)

  return cesta

main()