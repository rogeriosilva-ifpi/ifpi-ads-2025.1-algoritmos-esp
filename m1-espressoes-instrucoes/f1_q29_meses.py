# 29. Leia um número inteiro de meses, 
# calcule e escreva quantos anos e 
# quantos meses ele corresponde.

# Entrada
meses = int(input('Meses: '))

# Processamento
anos = meses // 12
meses_sobraram = meses % 12

# Saída
print(f'{meses} meses equivalem a {anos} ano(s) e {meses_sobraram} meses')