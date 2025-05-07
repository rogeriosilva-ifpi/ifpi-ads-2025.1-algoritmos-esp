def main():
  boi_id = int(input('ID: '))
  menor, menor_id = None, None
  maior, maior_id = None, None
  
  while boi_id != 0:
    boi_kg = float(input('Peso (kg): '))
    # maior
    if not maior or boi_kg > maior:
      maior = boi_kg
      maior_id = boi_id
    
    if not menor or boi_kg < menor:
      menor = boi_kg
      menor_id = boi_id

    boi_id = int(input('ID: '))
  

  if maior:
    print(f'Maior Boi é o ID={maior_id} com {maior}kg')
    print(f'Menor Boi é o ID={menor_id} com {menor}kg')

  print('Fim.')



main()