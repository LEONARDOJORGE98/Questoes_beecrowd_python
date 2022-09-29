valores = str(input()).split()

h1 = int(valores[0])
h2 = int(valores[1])

tempo1 = h2 - h1
tempo2 = (24 - h1) + h2

if h1 < h2:
  print('O JOGO DUROU {} HORA(S)'.format(tempo1))

elif h1 == h2:
  print('O JOGO DUROU 24 HORA(S)')

else:
  print('O JOGO DUROU {} HORA(S)'.format(tempo2))