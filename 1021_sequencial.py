valor = float(input())

nota100 = valor // 100
resto100 = valor % 100

nota50 = resto100 // 50
resto50 = resto100 % 50

nota20 = resto50 // 20
resto20 = resto50 % 20

nota10 = resto20 // 10
resto10 = resto20 % 10

nota5 = resto10 // 5
resto5 = resto10 % 5

nota2 = resto5 // 2
resto2 = resto5 % 2

moeda1 = resto2 // 1
resto1 = resto2 % 1

resto1 = (round(resto1,3)*100)

moeda050 = resto1 // 50
resto050 = resto1 % 50

moeda025 = resto050 // 25
resto025 = resto050 % 25

moeda010 = resto025 // 10
resto010 = resto025 % 10

moeda005 = resto010 // 5
resto005 = resto010 % 5

moeda001 = resto005 // 1

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(nota100))
print('{:.0f} nota(s) de R$ 50.00'.format(nota50))
print('{:.0f} nota(s) de R$ 20.00'.format(nota20))
print('{:.0f} nota(s) de R$ 10.00'.format(nota10))
print('{:.0f} nota(s) de R$ 5.00'.format(nota5))
print('{:.0f} nota(s) de R$ 2.00'.format(nota2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(moeda1))
print('{:.0f} moeda(s) de R$ 0.50'.format(moeda050))
print('{:.0f} moeda(s) de R$ 0.25'.format(moeda025))
print('{:.0f} moeda(s) de R$ 0.10'.format(moeda010))
print('{:.0f} moeda(s) de R$ 0.05'.format(moeda005))
print('{:.0f} moeda(s) de R$ 0.01'.format(moeda001))