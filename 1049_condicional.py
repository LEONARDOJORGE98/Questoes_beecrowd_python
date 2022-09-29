entrada1 = str(input())
entrada2 = str(input())
entrada3 = str(input())

if entrada1 == 'vertebrado':
  
  if entrada2 == 'ave':
    if entrada3 == 'carnivoro':
      print('aguia')
    if entrada3 == 'onivoro':
      print('pomba')
  
  if entrada2 == 'mamifero':
    if entrada3 == 'onivoro':
      print('homem')
    if entrada3 == 'herbivoro':
      print('vaca')

if entrada1 == 'invertebrado':

  if entrada2 == 'inseto':
    if entrada3 == 'hematofago':
      print('pulga')
    if entrada3 == 'herbivoro':
      print('lagarta')

  if entrada2 == 'anelideo':
    if entrada3 == 'hematofago':
      print('sanguessuga')
    if entrada3 == 'onivoro':
      print('minhoca')