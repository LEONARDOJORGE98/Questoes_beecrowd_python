maior = 0
posicao = 1

for c in range(1,5):
  n = int(input())
 
  if n > maior:
    maior = n
    posicao = c

print(maior)
print(posicao)