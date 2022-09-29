codigo = str(input()).split()

x = int(codigo[0])
y = int(codigo[1])

cachorroquente = 4.00
xsalada = 4.50
xbacon = 5.00
torradasimples = 2.00
refrigerante = 1.50

if x == 1:
  print('Total: R$ {:.2f}'.format(cachorroquente * y))

if x == 2:
  print('Total: R$ {:.2f}'.format(xsalada * y))

if x == 3:
  print('Total: R$ {:.2f}'.format(xbacon * y))

if x == 4:
  print('Total: R$ {:.2f}'.format(torradasimples * y))

if x == 5:
  print('Total: R$ {:.2f}'.format(refrigerante * y))