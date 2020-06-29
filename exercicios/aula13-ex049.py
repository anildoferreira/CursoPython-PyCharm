print('-=' * 15)
print('CALCULANDO TABUADA')
print('-=' * 15)


n= int(input('Digite um número para tabuada: '))
for c in range(0, 11, 1):
    t = n * c
    print('{} x {} = {}'.format(n, c, t))


