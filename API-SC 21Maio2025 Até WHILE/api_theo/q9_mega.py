def main():
    print('=== Mega-Sena ===')

    premio = float(input("Quanto é o prêmio?: "))

    premio_restante = premio * 0.80

    qtd_amigo = []
    
    
    
    while True:
        amigo = int(input("Quanto?: "))
        qtd_amigo.append(amigo)
        
        if amigo == 0:
            break

    print(premio_restante)
       

main()