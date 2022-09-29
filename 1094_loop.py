n = int(input())

coelho = sapo = rato = 0

for c in range(n):
  entrada = input().split()

  if entrada[1] == 'C':
    coelho += int(entrada[0])

  if entrada[1] == 'R':
    rato += int(entrada[0])

  if entrada[1] == 'S':
    sapo += int(entrada[0])

total = coelho + sapo + rato

porccoelho = coelho / total * 100
porcsapo = sapo / total * 100
porcrato = rato / total * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelho))
print('Total de ratos: {}'.format(rato))
print('Total de sapos: {}'.format(sapo))
print('Percentual de coelhos: {:.2f} %'.format(porccoelho))
print('Percentual de ratos: {:.2f} %'.format(porcrato))
print('Percentual de sapos: {:.2f} %'.format(porcsapo))
