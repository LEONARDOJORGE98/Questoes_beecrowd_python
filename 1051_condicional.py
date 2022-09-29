entrada = float(input())

if 0.00 <= entrada <= 2000.00:
  print('Isento')

if 2000.01 <= entrada <= 3000.00:
  imposto = (entrada - 2000.00) * 8 / 100
  print('R$ {:.2f}'.format(imposto))

if 3000.01 <= entrada <= 4500.00:
  imposto = ((entrada - 3000) * 18 / 100) + 80
  print('R$ {:.2f}'.format(imposto))

if entrada > 4500.00:
  imposto = ((entrada - 4500) * 28 / 100) + 80 + 270
  print('R$ {:.2f}'.format(imposto))