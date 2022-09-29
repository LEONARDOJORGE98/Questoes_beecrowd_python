gasolina = alcool = disel = 0
while True:
  entrada = int(input())

  if entrada == 1:
    alcool += 1

  elif entrada == 2:
    gasolina += 1

  elif entrada == 3:
    disel += 1

  elif entrada == 4:
    break
print(f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDisel {disel}")
  