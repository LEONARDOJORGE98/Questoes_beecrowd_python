media = 0
cont = 0
while True:

  X = float(input())

  if X < 0 or 10 < X:
    print('nota invalida')

  else:
    cont += 1
    media += X/2
  
  if cont == 2:
    print(f'media = {(media):.2f}')
    break
    