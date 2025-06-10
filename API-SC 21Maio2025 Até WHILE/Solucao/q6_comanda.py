from q1_number_utils import obter_inteiro_faixa, obter_inteiro_minimo


def main():

  menu = '''
  >>>>> BAR DO CAIUS <<<<<
  1 - Novo Item
  2 - Conta
  3 - Pagar
  0 - Encerrar

  >>> '''

  valor_total = 0
  contador_cerveja = 0

  opcao = obter_inteiro_faixa(menu, 0, 3)

  while opcao != 0:
    if opcao == 1:
      entrada = input('Pedido: ')
      qtd = int(entrada.split()[0])
      item = entrada.split()[1]

      if item == 'C':
        valor_total = valor_total + qtd * 9
        contador_cerveja += qtd
      elif item == 'T':
        valor_total = valor_total + qtd * 39
      elif item == 'A':
        valor_total = valor_total + qtd * 5
      else:
        print('Item inválido!')
    elif opcao == 2:
      servico = calcular_servico(contador_cerveja, valor_total)
      total_a_pagar = valor_total + servico
      mostrar_conta(valor_total, servico, total_a_pagar)
      
    elif opcao == 3:
      servico = calcular_servico(contador_cerveja, valor_total)
      
      total_a_pagar = valor_total + servico
      mostrar_conta(valor_total, servico, total_a_pagar)
      qtd_pessoas = obter_inteiro_minimo('Pessoas: ', 1)
      
      print(f'Valor por Pessoa: R$ {total_a_pagar / qtd_pessoas}')

    opcao = obter_inteiro_faixa(menu, 0, 3) 

  print('Fim.')


def mostrar_conta(valor_total, servico, total_a_pagar):
  print('>>>> Conta: <<<')
  print(f'Consumo R$ {valor_total:.2f}')
  print(f'Serviço R$ {servico:.2f}')
  print(f'Total a pagar R$ {total_a_pagar:.2f}')
  print('---------------------------------')
      

def calcular_servico(contador_cerveja, valor_total):
  if contador_cerveja > 10 or valor_total > 200:
    return 0
  
  return valor_total * 10 / 100

main()