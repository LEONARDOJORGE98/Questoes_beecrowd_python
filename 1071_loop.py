x = int(input())
y = int(input())
soma = 0

if x > y:
  for c in range(y + 1, x):
    if c % 2 != 0:
      soma += c

elif y > x:
  for c in range (x + 1, y):
    if c % 2 !=0:
      soma += c
      
print(soma)