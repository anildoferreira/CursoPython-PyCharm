kmRodados = float(input('Quantos km vc rodou? '))
diasUsados = int(input('Durante quantos dias? '))
pagar = kmRodados * 0.15 + diasUsados * 60
print('O valor a se pagar é de R$ {:.2f}'.format(pagar))

