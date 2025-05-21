def main():
    valor_conta = 0
    total_cervejas = 0
    while True:
        pedido = input('Adicionar item a conta (digite sair para parar de inserir e receber o valor da conta): ')
        if pedido == 'sair':
            break
        n = int(pedido.split()[0])
        tipo = pedido.split()[1]
        if tipo == 'C':
            valor_conta += n * 9
            total_cervejas += n
        if tipo == 'T':
            valor_conta += n * 39
        if tipo == 'A':
            valor_conta += n * 5
    qtd_pessoas = int(input('Quantidade de pessoaas : '))
    valor_pessoa = valor_conta / qtd_pessoas
    taxa_servico = valor_conta * 0.10
    valor_conta_acressimo = valor_conta + taxa_servico
    if total_cervejas > 10 or valor_conta > 200:
        print(f'O valor da conta é {valor_conta}R$ e o valor por pessoa é {valor_pessoa:.1f}R$')
        print('O valor da taxa de serviço foi : 0')
        print(f'O valor do total com taxa de serviço é : {valor_conta:.1f}')
    else:
        print(f'O valor da conta é {valor_conta}R$ e o valor por pessoa é {valor_pessoa:.1f}R$')
        print(f'O valor da taxa de serviço foi : {taxa_servico:.1f}R$')
        print(f'O valor do total com taxa de serviço é : {valor_conta_acressimo:.1f}R$')
main()