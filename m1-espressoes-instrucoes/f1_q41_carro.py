# 41. O custo ao consumidor de um carro novo é a 
# soma do custo de fábrica com a percentagem do
# distribuidor (aplicado sobre o valor de 
# fábrica com impostos) 
# e dos impostos (aplicados ao custo de fábrica). 
# Supondo que a percentagem do distribuidor
# seja de 28% e os impostos de 45%, escreva 
# um algoritmo que leia o custo de fábrica de um carro 
# e escreva o custo ao consumidor.

# Entrada 
custo_fabrica = float(input('Custo Fábrica: '))
perc_impostos = int(input('Impostos: '))
perc_distribuidor = int(input('Distribuidor: '))

# Processamento
impostos = custo_fabrica * (perc_impostos/100)
distribuidor = (custo_fabrica + impostos) * (perc_distribuidor/100)

valor_carro = custo_fabrica + impostos + distribuidor

# Saída (f-string)
print(f'O valor do Carro é R$ {valor_carro:.2f}')