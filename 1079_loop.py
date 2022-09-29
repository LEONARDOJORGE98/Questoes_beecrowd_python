n = int(input())
lista = []

for c in range(n):
  nota = input().split()
  media = ((float(nota[0]) * 2) + (float(nota[1]) * 3) + (float(nota[2]) * 5)) / 10

  lista.append(media)

for p in lista:
  print('{:.1f}'.format(p))