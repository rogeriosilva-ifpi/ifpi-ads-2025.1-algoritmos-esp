# 32. Leia um número inteiro (3 dígitos), c
# calcule e escreva a diferença entre o número e seu inverso.

# Entrada
numero = int(input('Número: '))

# Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = unidade*100 + dezena*10 + centena

soma = numero + inverso

# Saída
# print(f'C = {centena}')
# print(f'D = {dezena}')
# print(f'U = {unidade}')

print(f'A soma de {numero} com {inverso} é igual a {soma}')