def main():
    numero = int(input('Digite um número: '))
    cont = 1
    soma = 0
    while numero != 0:
        numero = int(input('Digite outro número: '))
        if numero % 2 == 0:
            soma += cont
            cont += 1

        elif numero == 0:
            media = soma / cont
            print(media)

main()


# faltou interpretar a questão.





