entrada = str(input()).split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = (B ** 2 - 4 * A * C)

if delta > 0 and A != 0:
  x1 = (- B + (delta) ** (1/2)) / (2* A)
  x2 = (- B - (delta) ** (1/2)) / (2* A)
  
  print('R1 = {:.5f}'.format(x1))
  print('R2 = {:.5f}'.format(x2))

else:
  print('Impossivel calcular')