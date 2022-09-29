X = []

for i in range(10):
  entrada = int(input())

  if entrada <= 0:
    X.append(1)
  else:
    X.append(entrada)

for i in range(len(X)):
  print(f'X[{i}] = {X[i]}')