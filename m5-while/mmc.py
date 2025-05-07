def main():
  num1 = int(input('Num 1: '))
  num2 = int(input('Num 2: '))

  resultado = mmc(num1, num2)

  print(f'O MMC({num1}, {num2}) = {resultado}')


def mmc(m, n):
  valor = 1

  while not (valor % m == 0 and valor % n == 0):
    valor += 1

  return valor

main()