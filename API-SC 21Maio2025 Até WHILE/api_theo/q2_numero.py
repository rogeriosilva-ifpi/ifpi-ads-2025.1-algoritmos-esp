def main():
       qtd_seguencia = int(input('Quantas seguências vôce quer?: '))
       cada_seguencia = []

       while qtd_seguencia >= 1:
            numero = int(input('Número (0 para sair.): '))
                
            if numero == 0:
                break                
                     
            cada_seguencia.append(numero)
            qtd_seguencia += 1




main()




