# 12. Leia o salário de um trabalhador e 
# escreva seu novo salário com um aumento de 25%.

# entrada
salario = float(input('Salário: '))
percentual = float(input('Reajuste (%): '))

# processamento
aumento = (salario / 100) * percentual
novo_salario = salario + aumento

# saída
print('Seu aumento será de R$', aumento)
print('Portanto, seu novo salário será: R$', novo_salario)