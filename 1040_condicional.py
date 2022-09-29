notas = str(input()).split()

n1 = float(notas[0]) * 2
n2 = float(notas[1]) * 3
n3 = float(notas[2]) * 4
n4 = float(notas[3]) * 1

media = (n1 + n2 + n3 + n4) / 10

if media >= 7.0:
  print('Media: {:.1f}'.format(media))
  print('Aluno aprovado.')
  
if media < 5.0:
  print('Media: {:.1f}'.format(media))
  print('Aluno reprovado.')

if media >= 5.0 and media <= 6.9:
  print('Media: {:.1f}'.format(media))
  print('Aluno em exame.')
  notadoexame = float(input())
  print('Nota do exame: {:.1f}'.format(notadoexame))

  novamedia = (media + notadoexame) / 2

  if novamedia >= 5.0:
    print('Aluno aprovado.')
    print('Media final: {:.1f}'.format(novamedia))

  else:
    print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(novamedia))