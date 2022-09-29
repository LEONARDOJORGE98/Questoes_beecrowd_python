valores = str(input()).split()

h1 = int(valores[0])
m1 = int(valores[1])
h2 = int(valores[2])
m2 = int(valores[3])

if h2 > h1 and m2 > m1:
  tempo1 = (h2 - h1)
  tempo2 = (m2 - m1)
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 == h2 == m1 == m2:
  print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

if h2 > h1 and m2 < m1:
  tempo1 = (h2 - h1) - 1
  tempo2 = 60 - (m1 - m2)
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 > h2 and m2 > m1:
  tempo1 = (24 - h1) + h2
  tempo2 = (m2 - m1)
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 > h2 and m2 < m1:
  tempo1 = (24 - h1) + h2 - 1
  tempo2 = 60 - (m1 - m2)
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 == h2 and m2 < m1:
  tempo1 = 23
  tempo2 = 60 - (m1 - m2)
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 == h2 and m2 > m1:
  tempo1 = 0
  tempo2 = m2 - m1
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 > h2 and m2 == m1:
  tempo1 = (24 - h1) + h2
  tempo2 = 0
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))

if h1 < h2 and m2 == m1:
  tempo1 = (h2 - h1)
  tempo2 = 0
  print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempo1, tempo2))