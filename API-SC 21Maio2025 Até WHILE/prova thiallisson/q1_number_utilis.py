#def main():

def receber_inteiro():
    n1 = int(input("Digite um número inteiro:"))
    while n1 // n1 == 0:
        return print("Número inteiro")

     
def receber_inteiro_posi():
    n1 = int(input("Digite um número inteiro positivo:"))
    while n1 >= 0:
        return print("Inteiro +")
      

def receber_inteiro_neg():
    n1 = int(input("Digite um número inteiro negativo:"))
    while n1 <= 0:
        return print("Inteiro -")

def receber_inteiro_min(n1):
    n2 = int(input(f"Digite um número inteiro de minímo {n1}:"))
    while n1 <= n2:
        return print(f"Número maior que {10}:")
    else:
        print("Numero invalido")

def receber_inteiro_max(n1):
    n2 = int(input(f"Digite um número inteiro de máximo {n1}:"))
    while n1 >= n2:
        return print(f"Número menor que {n1}:")
    else:
        print("Numero invalido")

def receber_inteiro_entre(n1, n2):
    numero = int(input("Digite um número inteiro negativo:"))
    while numero >= n1 and numero <= n2:
        return print(f"Numero entre {n1} e {n2}")
    else:
        print("Numero invalido")

#receber_inteiro()
#receber_inteiro_posi()
#receber_inteiro_neg()
#receber_inteiro_min(10)
#receber_inteiro_max(10)
#receber_inteiro_entre()

#main()