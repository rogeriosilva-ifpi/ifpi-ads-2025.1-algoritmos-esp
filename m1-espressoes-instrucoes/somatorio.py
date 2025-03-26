# Somatorio de N até M (M e N inteiros, com M maior que N)
limite_inferior = int(input('Limite Inferior: '))
limite_superior = int(input('Limite Superior: '))

# processamento
valor_par = limite_superior + limite_inferior
qtd_pares = (limite_superior - limite_inferior + 1) / 2
somatorio = valor_par * qtd_pares

# saída
print(somatorio)