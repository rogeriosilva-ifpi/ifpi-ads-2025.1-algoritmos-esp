from math import sqrt, pi

def main():

  valor = 2*sqrt(2) / 9801
  
  resultado = valor * calcular_adicao()

  print(1/pi, '==', resultado)


def calcular_adicao():
  k = 0
  termo = calcular_termo(k)
  somatorio = termo

  while termo >= 10 ** 15:
    k = k + 1
    termo = calcular_termo(k)
    somatorio = somatorio + termo

  return somatorio


def calcular_termo(k):
  numerador = fatorial(4*k) * (1103 + (26390 * k))
  denominador = (fatorial(k)**4) * (396**(4*k))
  
  termo = (numerador / denominador)

  return termo


def fatorial(n):
  if n == 0 or n == 1:
    return 1

  return n * fatorial(n - 1)

main()