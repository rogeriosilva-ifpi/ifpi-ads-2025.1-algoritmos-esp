
def main():
    qtd_sequencias = int(input("Digite a quantidade de sequências: "))
    

#1. Pedir números da sequência
    soma_dos_numeros = 0
    soma_numeros_pares = 0
    menor_numero = 0
    maior_numero = 0
    qtd_divisor = qtd_sequencias
    media_seq = soma_dos_numeros

    while(qtd_sequencias > 0):
        numero = int(input("Digite um número inteiro:"))
        soma_dos_numeros = numero
        
        while (numero != 0):
            numero = int(input("Digite um número inteiro:"))
            soma_dos_numeros = soma_dos_numeros + numero

            if (numero % 2 == 0):
             soma_numeros_pares = soma_numeros_pares + numero
            if (numero > maior_numero) and numero > 0:
             maior_numero = numero
            else:
             menor_numero = numero

            qtd_sequencias = qtd_sequencias - 1
    print(f'QTD SEQUENCIAS: {qtd_sequencias}')
    print(f'Soma números: {soma_dos_numeros}')
    print(f'A média de todas as sequências é: {media_seq}')
    print (f'A soma dos números pares de cada sequência é {soma_numeros_pares}')
    print(f'O menor número digitado foi {menor_numero}')
    print(f'O maior número digitado foi {maior_numero}')



main()

