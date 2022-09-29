while True:


  X,Y = list(map(int,input().split()))

  if 0 < X and  0 < Y:
    print('primeiro')

  elif X < 0 and 0 < Y: 
    print('segundo')       

  elif X < 0 and Y < 0:
    print('terceiro')

  elif 0 < X and Y < 0:
    print('quarto')

  else:
    break  