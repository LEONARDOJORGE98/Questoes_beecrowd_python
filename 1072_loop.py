n = int(input())
somain = 0
somaout = 0

for c in range(n):
  x = int(input())

  if 10 <= x <= 20:
    somain += 1

  if x < 10 or x > 20:
    somaout += 1

print('{} in'.format(somain))
print('{} out'.format(somaout))