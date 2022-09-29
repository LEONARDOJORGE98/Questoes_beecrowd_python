valores = str(input()).split()

A = int(valores[0])
B = int(valores[1])

if B / A == (B // A) or A / B == (A // B):
  print('Sao Multiplos')

else:
  print('Nao sao Multiplos')