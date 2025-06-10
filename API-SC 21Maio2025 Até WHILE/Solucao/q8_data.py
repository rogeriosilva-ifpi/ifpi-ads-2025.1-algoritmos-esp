from q1_number_utils import obter_inteiro_faixa


def main():
  dia_1 = obter_inteiro_faixa('Dia: ', 1, 30)
  mes_1 = obter_inteiro_faixa('Mês: ', 1, 12)
  ano_1 = obter_inteiro_faixa('Ano: ', 1, 3000)
  dia_2 = obter_inteiro_faixa('Dia: ', 1, 30)
  mes_2 = obter_inteiro_faixa('Mês: ', 1, 12)
  ano_2 = obter_inteiro_faixa('Ano: ', 1, 3000)

  dias_1 = dia_1 + 30*mes_1 + 12*30*ano_1
  dias_2 = dia_2 + 30*mes_2 + 12*30*ano_2

  diff = dias_2 - dias_1

  if diff < 0:
    diff = diff * -1

  anos = diff // 360
  resto = diff % 360
  meses = resto // 12
  dias = resto % 12

  # Saída (Formatar saída) - estou cansado mas sei fazer.
  print(f'{anos} anos, {meses} meses e {dias} dias')


main()