def main():
  n = int(input())
  qtd = n
  somatorio = 0

  while n > 0:
    somatorio = somatorio + int(input())
    n -= 1

  media = somatorio / qtd

  print('Média -->', f'{media:.2f}')

main()
