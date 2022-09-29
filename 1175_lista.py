N = []

for i in range(4):
  entrada = int(input())
  N.append(entrada)

N1 = []
for i in range(len(N)):
  N1.append(N[len(N)-1-i])
  print(f'N[{i}] = {N1[i]}')
  
N = []

for i in range(20):
  entrada = int(input())
  N.append(entrada)


for i in range(len(N)//2):
  aux =  N[i]
  N[i] = N[len(N)-1-i]
  N[len(N)-1-i] = aux

for i in range(len(N)):
  print(f'N[{i}] = {N[i]}')
