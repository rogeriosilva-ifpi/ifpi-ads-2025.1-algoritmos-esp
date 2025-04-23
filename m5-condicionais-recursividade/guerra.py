def main():
  ano_nascimento = int(input('Ano Nascimento: '))
  sexo = input('Sexo: ')

  idade = 2025 - ano_nascimento
  print(f'Em 2025, vc tem {idade} anos')

  if eh_maior_idade(idade) and not eh_idoso(idade) and not eh_mulher(sexo):
    print('Parabéns, vc foi convocado!')
  else:
    print('Sinto muito, vai ficar orando em casa')

# funcoes booleanas
def eh_maior_idade(idade):
  return idade >= 18
  
def eh_idoso(idade):
  return idade >= 60
  
def eh_homem(sexo):
  return sexo == 'M'

def eh_mulher(sexo):
  return not eh_homem(sexo)
  

main()