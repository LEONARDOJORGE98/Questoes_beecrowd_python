gremio = inter = empates = grenais = 0
continuacao = True

while continuacao:

  entrada = list(map(int,input().split()))
  grenais += 1

  if entrada[0] > entrada[1]:
    inter += 1

  elif entrada[0] < entrada[1]:
    gremio += 1

  else:
    empates += 1

  print('Novo grenal (1-sim 2-nao)')
  novo_grenal = int(input())

  if novo_grenal == 2:
    continuacao = False
    
    print(f'{grenais} grenais')
    print(f'Inter:{inter}')
    print(f'Gremio:{gremio}')
    print(f'Empates:{empates}')

    if inter > gremio:
      print(f'Inter venceu mais')

    elif gremio > inter:
      print(f'Gremio venceu mais')

    else:
      print(f'Nao houve vencedor')  