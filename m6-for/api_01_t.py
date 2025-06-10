def main():
  nome = input('Nome: ')

  tamanho = len(nome) 

  if tamanho % 2 != 0:
    mostrar_divisores(tamanho)
  else:
    mostrar_multiplos(tamanho)


def mostrar_divisores(numero):
  for d in range(1, numero + 1, 1):
    if numero % d == 0:
      print(d)


def mostrar_multiplos(numero):
  for i in range(1, numero+1, 1):
    print(numero * i)


main()