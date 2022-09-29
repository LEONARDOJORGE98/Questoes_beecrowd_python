valores = str(input()).split()

ladoA = float(valores[0])
ladoB = float(valores[1])
ladoC = float(valores[2])

perimetro = ladoA + ladoB + ladoC
area = ((ladoA + ladoB) * ladoC) / 2

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
  print('Perimetro = {:.1f}'.format(perimetro))

else:
  print('Area = {}'.format(area))