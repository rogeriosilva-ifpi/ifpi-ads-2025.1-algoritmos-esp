def main():
    numeros = []
    numeros_media = 0
    contador = 0
    numeros_pares = 0
    qtd_numeros = []
    while True:
        num_inteiro = inteiro()
        if num_inteiro == 0:
            break
        if num_inteiro % 2 == 0:
            numeros_pares += (num_inteiro)
            numeros.append(num_inteiro)
            numeros_media += num_inteiro
            qtd_numeros.append(num_inteiro)
            contador += 1
        if num_inteiro % 2 == 1:
            numeros.append(num_inteiro)
            qtd_numeros.append(num_inteiro)
            numeros_media += num_inteiro
            contador += 1
    if numeros:
        menor = min(numeros)
        maior = max(numeros)
    print(f'A soma dos numeros pares de cada sequencia é : {numeros_pares}')
    print(f'A média de todos os numeros digitados é : {numeros_media // contador}')
    print(f'O menor numero digitado da sequencia é : {menor}')
    print(f'O maior numero digitado da sequencia é : {maior}')
def inteiro():
    while True:
        entrada = input('Digite o valor inteiro :')
        try:
            num = int(entrada)
            return num
        except ValueError:
            print('Valor inválido, digite outro!!!')
            return inteiro()
        
    
main()