valores = str(input()).split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

maior = A or B or C
meio = A or B or C
menor = A or B or C

if A > B and A > C:
  maior = A

  if B > C:
    meio = B
    menor = C
  else:
    meio = C
    menor = B

if B > A and B > C:
  maior = B

  if A > C:
    meio = A
    menor = C

  else:
    meio = C
    menor = A

if C > A and C > B:
  maior = C

  if A > B:
    meio = A
    menor = B

  else:
    meio = B
    menor = A

if maior >= meio + menor:
  print('NAO FORMA TRIANGULO')

else:

  if maior ** 2 == (meio ** 2) + (menor ** 2):
    print('TRIANGULO RETANGULO')

  if maior ** 2 > (meio ** 2) + (menor ** 2):
    print('TRIANGULO OBTUSANGULO')

  if maior ** 2 < (meio ** 2) + (menor ** 2):
    print('TRIANGULO ACUTANGULO')

  if A == B and A == C and C == B:
    print('TRIANGULO EQUILATERO')

  if A == B and A != C or B == C and B != A or C == A and C != B:
    print('TRIANGULO ISOSCELES')
