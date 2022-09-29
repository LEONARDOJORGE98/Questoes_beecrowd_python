A = []
for i in range(100):
  entrada = float(input())
  A.append(entrada)

for n in range(len(A)):
  if A[n] <= 10:
    print(f'A[{n}] = {A[n]:.1f}')
