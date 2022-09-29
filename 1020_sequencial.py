idade = int(input())

anoint = idade // 365
anoresto = idade % 365

meses = anoresto // 30

dias = anoresto % 30

print('{} ano(s)'.format(anoint))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))