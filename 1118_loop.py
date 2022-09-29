media = cont = 0
continuar = True
while continuar == True:

  entrada = float(input())

  if entrada < 0 or 10 < entrada:
    print('nota invalida')

  else:
    cont += 1
    media += entrada/2

    if cont == 2:
      print(f'media = {media:.2f}')
      cont = 0
      media = 0

      while True:

        print('novo calculo (1-sim 2-nao)')
        novo_calculo = int(input())

        if novo_calculo == 1:
          break

        elif novo_calculo == 2:
          continuar = False
          break