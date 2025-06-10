while True:

    cerveja = input('Digite "c" para pedir cerveja: ')
    if cerveja == "c":
        break
    print('Digite "c" para pedir uma cerveja')

valor_cerveja = 9
quantidade_cerveja = int(input('Digite a quantidade de pedidos de cervejas: '))
total_cervejas = quantidade_cerveja * valor_cerveja

while True:
    
    tira_gosto = input('Digite "t" para pedir tira gosto: ')
    if tira_gosto == 't':
        break
    print('Digite "t" para pedir um tira gosto')

valor_tira_gosto = 39
quantidade_tira_gosto = int(input('Digite a quantidade de pedidos de tira gosto: '))
total_tira_gosto = valor_tira_gosto * quantidade_tira_gosto

while True:

    agua = input('Digite "a" para pedir agua: ')
    if agua == 'a':
        break
    print('Digite "c" para pedir a água')

valor_agua = 5
quantidade_agua = int(input('Digite a quantidade de pedidos de água: '))
total_de_agua = valor_agua * quantidade_agua

total = total_cervejas + total_tira_gosto + total_de_agua


    
if total > 200 or quantidade_cerveja > 10:
    valor_da_conta = total
else:
    valor_da_conta = (total * 0.10) + total
        

taxa_de_serviço = total * 0.10
quantidade_de_pessoas = int(input('Digite a quantidade de pessoas que irão pagar: '))
valor_por_pessoa = valor_da_conta / quantidade_de_pessoas


print('-------------------------------------------------------')
print(f'O valor da conta: R${valor_da_conta:.2f}')
print(f'O valor por pessoa: R${valor_por_pessoa}')
print(f'Valor da taxa de serviço: R$ {taxa_de_serviço:.2f}')
print(f'O valor com taxa de serviço: R$ {valor_da_conta:.2f}')


# Faltou organizar em um Sistema em si.
# Ter um Menu que gira até que se deseje.
# Totalmente sem funções. 
# A lógica de pedir apenas produto por vez não condiz com o pedido e ir até o final. 
