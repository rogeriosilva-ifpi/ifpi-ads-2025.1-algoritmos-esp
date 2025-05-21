def main():
    valor_mega = int(input('Digite o valor da mega sena: '))
    mega_pos_imposto = valor_mega-(valor_mega*(20/100))
    amigo = 0
    valor_premio_individual = 0
    maior_premio_individual = 0
    menor_premio_individual = 9999

    while True:
        amigo += 1
        valor_bilhete = float(input(f'Digite o valor do bilhete do amigo {amigo} [0 não contribui e sai da contagem]:R$ '))
        if valor_bilhete == 0:
            break
        while valor_bilhete < 0:
            print('Valor errado, tente novamente.')
            valor_bilhete = float(input(f'Digite o valor do bilhete do amigo {amigo} [0 não contribui e sai da contagem]:R$ '))
        valor_premio_individual = (mega_pos_imposto/valor_bilhete)
        if valor_premio_individual > maior_premio_individual:
            maior_premio_individual = valor_premio_individual
        elif valor_premio_individual < menor_premio_individual:
            menor_premio_individual = valor_premio_individual
    
    print(f'Prêmio com os 20% de imposto abatidos: R$ {mega_pos_imposto:.2f}')
    print(f'Maior Prêmio Individual: R$ {maior_premio_individual:.2f}')
    print(f'Menor Prêmio Individual: R$ {menor_premio_individual:.2f}')


main()