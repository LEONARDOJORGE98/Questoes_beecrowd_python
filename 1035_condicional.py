entrada = str(input()).split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])
D = int(entrada[3])

par = A % 2

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and par == 0:
  print('Valores aceitos')
  
else:
  print('Valores nao aceitos')