def main():

    num = int(input('Digite um número: '))
    n_sequencias = 0
    final_numeros = 0
    soma_pares = 0
    soma_total = 0
    maior_numero = 0
    menor_numero = 9999

    print(num)
    while n_sequencias < num:
        n_sequencias += 1
        final_numeros += num*10
        print(final_numeros)
        soma_total += final_numeros
        if final_numeros % 2 == 0:
            soma_pares += final_numeros
        if final_numeros > maior_numero:
            maior_numero = final_numeros
        if final_numeros < menor_numero:
            menor_numero = final_numeros

    print('Soma dos numeros pares das sequencias:', soma_pares)
    print('Média de todas as sequências:', soma_total/n_sequencias)
    print('Maior número:', maior_numero)
    print('Menor número:', menor_numero)

main()

# Faltou interpretar sequências