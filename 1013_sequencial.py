valores = str(input()).split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])

maiorab = (A + B + abs(A - B)) / 2

maior_de_todos = (maiorab + C + abs(maiorab - C)) / 2

print('{} eh o maior'.format(int(maior_de_todos)))
