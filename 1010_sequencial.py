entrada1 = input().split()

codigo1 = entrada1[0]
quantidade1 = int(entrada1[1])
valor1 = float(entrada1[2])

entrada2 = input().split()

codigo2 = entrada2[0]
quantidade2 = int(entrada2[1])
valor2 = float(entrada2[2])

total = (quantidade1 * valor1) + (quantidade2 * valor2)

print('TOTAL A PAGAR: R$ {:.2f}'.format(total))