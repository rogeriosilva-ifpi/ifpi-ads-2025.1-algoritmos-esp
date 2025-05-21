def main():
    valor_conta = 0
    taxa_servico = 0
    valor_com_taxa = 0
    qtd_cerveja = 0
    qtd_pessoas = 0
    c = 9
    t = 39
    a = 5

    menu = int(input("""------MENU------ 
    1 = INSERIR PRODUTOS
    2 = CALCULAR A CONTA
    3 = IMPRIMIR A CONTA                 
    4 = CONFIRMAR PAGAMENTO                
    """))

    if menu == 1:
        print("""PRODUTOS
    Cerveja ----------- 9 Reais
    Tira-Gosto -------- 39 Reais
    Água -------------- 5 Reais                   
    """)
        while True:
            inserir_produto = input('Digite a quantidade e o produto desejado [ex.: 1 C]: ')
            n = int(inserir_produto.split() [0])
            tipo = inserir_produto.upper().split() [1]
            if tipo == 'C':
                valor_conta += (n*c)
                qtd_cerveja += n
            elif tipo == 'T':
                valor_conta += (n*t)
            elif tipo == 'A':
                valor_conta += (n*a)
            confirma = int(input("""Deseja continuar?: 
        [1] CONTINUAR
        [0] PARAR
        """))
            if confirma == 0:
                break

    if menu == 2:
        print("CALCULANDO A CONTA...")
        print(f'Valor final da conta: R$ {valor_conta:.2f}')
        if valor_conta < 200 or qtd_cerveja < 10:
            taxa_servico = valor_conta * (10/100)
            valor_com_taxa = valor_conta + taxa_servico

    if menu == 3:
        print(""" IMPRIMINDO A CONTA... """)
        qtd_pessoas = int(input('Quantas pessoas irão pagar a conta: '))
        if valor_conta < 200 or qtd_cerveja < 10:
            valor_com_taxa
            valor_por_pessoa = valor_com_taxa/qtd_pessoas
            taxa_servico = valor_conta * (10/100)
            print(f'Valor da taxa de serviço: R$ {taxa_servico}')
            print(f'Valor da conta: R$ {valor_com_taxa:.2f} / Valor por pessoa: R$ {valor_por_pessoa:.2f}')
        else:
            valor_por_pessoa = valor_conta/qtd_pessoas
            print(f'Valor da conta: R$ {valor_com_taxa:.2f} / Valor por pessoa: R$ {valor_por_pessoa:.2f}')

    if menu == 4:
        valor_conta == 0 and valor_com_taxa == 0
        print(">>> CONTA DA MESA FOI PAGA E ZERADA <<<")

main()