def main():
  n = int(input())

  lista = list(range(1, n+1, 1))

  res = list(map(lambda x: x*2, lista))

  for item in res:
    print(item)


main()