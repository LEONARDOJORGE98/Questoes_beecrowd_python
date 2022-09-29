lista = []

n = int(input())

for c in range(n):
  
  x = input().split()

  x[0] = int(x[0])
  x[1] = int(x[1])
  
  if x[0] == x[1] or x[0] - x[1] == 1 or x[1] - x[0] == 1:

    soma = 0
    
    lista.append(soma)
        
  elif x[0] > x[1]:

    soma = 0

    for c in range(x[1] + 1, x[0]):

      if c % 2 != 0:

        soma += c
    lista.append(soma)

  elif x[0] < x[1]:

    soma = 0

    for c in range(x[0] + 1, x[1]):

      if c % 2 != 0:

        soma += c
      
    lista.append(soma)

for c in range(n):
  print(lista[c])