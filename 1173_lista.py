N = [0]*10
entrada = int(input())

N.insert(0,entrada)

mult = N[0]

for i in range(1,10):
  mult *= 2
  N.insert(i, mult)

for i in range(10):
  print(f'N[{i}] = {N[i]}')