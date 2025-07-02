# MAP, FILTER e REDUCE
def mapear(colecao, funcao_transformadora):
  cesta = []
  for item in colecao:
    item_transformado = funcao_transformadora(item)
    cesta.append(item_transformado)
  
  return cesta


def filtrar(colecao, funcao_criterio):
  cesta = []
  for item in colecao:
    if funcao_criterio(item):
      cesta.append(item)
  
  return cesta


def reduzir(colecao, funcao_redutora, valor_inicial):
  acumulado = valor_inicial
  for item in colecao:
    acumulado = funcao_redutora(acumulado, item)
  
  return acumulado