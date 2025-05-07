def main():
  numero = int(input('N: '))

  contador = 1
  quociente = numero // 10
  
  while quociente != 0:
    contador += 1
    quociente = quociente // 10
  
  print(contador)


main()