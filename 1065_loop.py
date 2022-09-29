cont = 0

for c in range (1, 6):
  entrada = int(input())

  if entrada % 2 == 0:
    cont += 1

print('{} valores pares'.format(cont))