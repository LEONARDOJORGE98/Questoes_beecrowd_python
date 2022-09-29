entrada = int(input())

for i in range(entrada):

  X,Y = list(map(int,input().split()))

  if Y == 0:
    print('divisao impossivel')

  
  else:
    divisao = X/Y
    print(f'{divisao:.1f}')

    