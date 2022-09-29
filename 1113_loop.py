while True:

  X,Y = list(map(int,input().split()))

  if X == Y:
    break

  else:
    if X < Y:
      print('Crescente')

    else:
      print('Decrescente')


