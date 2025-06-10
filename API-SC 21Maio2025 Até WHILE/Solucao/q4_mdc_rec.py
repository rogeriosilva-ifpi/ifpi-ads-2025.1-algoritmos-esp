from q1_number_utils import obter_inteiro_positivo


def main():
  num1 = obter_inteiro_positivo('Valor 1: ')
  num2 = obter_inteiro_positivo('Valor 2: ')

  cand_zero = num1//2 if num1 < num2 else num2//2

  valor = mdc(num1, num2, cand_zero)

  print(f'>> MDC({num1}, {num2}) == {valor}')


def mdc(a: int, b: int, leo: int):
  if a % leo == 0 and b % leo == 0:
    return leo

  return mdc(a, b, leo-1)


main()