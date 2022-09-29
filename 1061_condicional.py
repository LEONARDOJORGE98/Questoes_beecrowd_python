dia1 = str(input()).split()
hora1 = str(input()).split()
dia2 = str(input()).split()
hora2 = str(input()).split()

d1 = int(dia1[1])
h1 = int(hora1[0])
m1 = int(hora1[2])
s1 = int(hora1[4])

d2 = int(dia2[1])
h2 = int(hora2[0])
m2 = int(hora2[2])
s2 = int(hora2[4])

totaldia1 = (d1 * 24 * 60 * 60) + (h1 * 60 * 60) + (m1 * 60) + s1

totaldia2 = (d2 * 24 * 60 * 60) + (h2 * 60 * 60) + (m2 * 60) + s2

totalsegundos = totaldia2 - totaldia1

dias = totalsegundos // 86400
diasresto = totalsegundos % 86400
horas = diasresto // 3600
horasresto = diasresto % 3600
minutos = horasresto // 60
segundos = horasresto % 60

print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos))