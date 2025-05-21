def main():
    soma = 0
    media = 0 
    menor = 5
    maior = 5
    contador = 0
    soma_numeros = 0

    while True:
        n = int(input('Número (0 para sair.): '))
        contador += 1
         
        if n == 0:
            break

        if n % 2 == 0:
            soma += n

        if menor < n:
            menor = n

        if maior > n:
            maior = n

        soma_numeros += n

        media =  soma_numeros / contador

    print(f'\nA soma dos números pares é: {soma}')
    print(f'A média dos números é: {media:.2f}')
    print(f'O menor número é: {menor}')
    print(f'O maior número é: {maior} ')

main()




