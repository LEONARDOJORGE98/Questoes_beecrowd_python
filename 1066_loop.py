contpares = 0
contimpares = 0
contpositivos = 0
contnegativos = 0

for c in range (1, 6):
  entrada = int(input())

  if entrada % 2 == 0:
    contpares += 1

  if entrada % 2 != 0:
    contimpares += 1

  if entrada > 0:
    contpositivos += 1

  if entrada < 0:
    contnegativos += 1


print('{} valor(es) par(es)'.format(contpares))
print('{} valor(es) impar(es)'.format(contimpares))
print('{} valor(es) positivo(s)'.format(contpositivos))
print('{} valor(es) negativo(s)'.format(contnegativos))