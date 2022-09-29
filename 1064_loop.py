cont = 0
soma = 0

for c in range(1, 7):
  pos = float(input())
  
  if pos > 0:
    cont += 1
    soma += pos
    media = soma/cont


print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))