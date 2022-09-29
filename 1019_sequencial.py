tempo = int(input())

horas = tempo // 3600
horasresto = tempo % 3600

minutos = horasresto // 60
segundos = horasresto % 60

print('{}:{}:{}'.format(horas, minutos, segundos))