def menu():
    menu = '''Cerveja = R$ 9.00
Tira-gosto = R$ 39.00
Àgua = R$ 5.00 
\n1 C = 1X Cerveja
1 T = 1X Tira-gosto
1 A = 1X Àgua
'''
    print(menu)
    print(opcao(menu))

def opcao(menu):
    mensagem= input('Escolha: ')

menu()