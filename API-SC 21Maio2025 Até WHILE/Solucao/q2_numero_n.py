from q1_number_utils import obter_inteiro, obter_inteiro_positivo


def main():
  qtd_seq = obter_inteiro_positivo('N: ')
  contador = 0
  somatorio_geral = 0
  contador_geral = 0
  maior = None
  menor = None


  while contador < qtd_seq:
    print('Início Seq', contador)
    
    soma_pares = 0
    valor = obter_inteiro('Valor: ')
    while valor != 0:
      somatorio_geral = somatorio_geral + valor
      contador_geral += 1

      if valor % 2 == 0:
        soma_pares = soma_pares + valor
      valor = obter_inteiro('Valor: ')

      if menor == None or valor < menor:
        menor = valor

      if maior == None or valor > maior:
        maior = valor
    
    print(f'Soma dos Pares: {soma_pares}')
    print('Fim Seq', contador)

    contador += 1

  media = somatorio_geral / contador_geral
  print('Resumo:')
  print(f'Foram digitados {contador_geral} números')
  print(f'A média foi {media:.2f}')
  print(f'Menor valor: {menor}')
  print(f'Maior valor: {maior}')


main()