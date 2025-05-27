
contador = 0
soma = 0
todos_os_casos = []

# funções
def controle_de_casos(casos):
    if casos < 50:
        return "Em queda!"
    elif casos > 100 and casos < 150:
        return "Em estabilidade!"
    else:
        return "Em alta!"
    
#entrada

while True:
    casos = int(input('Quantos casos quer registrar(para sair digite "fim"): '))
    if casos == "fim":
        print("fim")
    break
todos_os_casos.append(casos)

#processamento

resultado2 = controle_de_casos(casos)

print(f'foram registrados: {todos_os_casos}casos! \n{resultado2}')
    

    
# Bem confuso. Faltou entender a questão.
