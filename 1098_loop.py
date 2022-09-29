I = 0
J = 0

while I < 2.1:

  for c in range(3):
  
    J += 1

    if I == (int(I)) or J == (int(J)):

      print('I={:.0f} J={:.0f}'.format(I, J))

    else:

      print('I={:.1f} J={:.1f}'.format(I, J))

  I += 0.2
  J = I