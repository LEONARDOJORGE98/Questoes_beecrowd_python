entrada = float(input())

if entrada <= 400.00:
  novo = entrada + (entrada / 100 * 15)
  reajuste = (entrada / 100 * 15)
  p = 15
  
if 400.01 <= entrada <= 800.00:
  novo = entrada + (entrada / 100 * 12)
  reajuste = (entrada / 100 * 12)
  p = 12

if 800.01 <= entrada <= 1200.00:
  novo = entrada + (entrada / 100 * 10)
  reajuste = (entrada / 100 * 10)
  p = 10

if 1200.01 <= entrada <= 2000.00:
  novo = entrada + (entrada / 100 * 7)
  reajuste = (entrada / 100 * 7)
  p = 7
  
if entrada > 2000.00:
  novo = entrada + (entrada / 100 * 4)
  reajuste = (entrada / 100 * 4)
  p = 4

  print('Novo salario: {:.2f}'.format(novo))
  print('Reajuste ganho: {:.2f}'.format(reajuste))
  print('Em percentual: {} %'.format(p))