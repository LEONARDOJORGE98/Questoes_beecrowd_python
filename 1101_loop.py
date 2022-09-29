soma = 0
while True:
  
  M,N = list(map(int,input().split()))

  if M <= 0 or N <= 0:
    break

  else:
    soma = 0
    menor = min(M,N)
    maior = max(M,N)

    for i in range(menor,maior+1):
      print(f'{i}',end=' ')
      soma += i

    print(f'Sum={soma}')
