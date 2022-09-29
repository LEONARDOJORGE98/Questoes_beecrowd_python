n = int(input())

lista = []

for c in range(n):
  entrada = int(input())
  lista.append(entrada)
  
for p in lista:
 
  if p == 0:
    print('NULL')

  elif p % 2 == 0 and p > 0:
    print('EVEN POSITIVE')

  elif p % 2 != 0 and p > 0:
    print('ODD POSITIVE')

  elif p % 2 == 0 and p < 0:
    print('EVEN NEGATIVE')

  else:
    print('ODD NEGATIVE')