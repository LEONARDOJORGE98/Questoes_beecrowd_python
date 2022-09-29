entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maior = meio = menor = 0

if a > b and a > c:
  maior = a
  if b > c:
    meio = b
    menor = c
  else:
    meio = c
    menor = b
  print(f'{menor}\n{meio}\n{maior}')
  print('')
  print(f'{a}\n{b}\n{c}')

if b > a and b > c:
  maior = b
  if a > c:
    meio = a
    menor = c
  else:
    meio = c
    menor = a
  print(f'{menor}\n{meio}\n{maior}')
  print('')
  print(f'{a}\n{b}\n{c}')

if c > a and c > b:
  maior = c
  if a > b:
    meio = a
    menor = b
  else:
    meio = b
    menor = a
  print(f'{menor}\n{meio}\n{maior}')
  print('')
  print(f'{a}\n{b}\n{c}')