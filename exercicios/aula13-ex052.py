n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if 0 == n % c:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mNúmero {} foi divisível \033[7m{} vezes\033[m'.format(n, tot))
if tot == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele não é primo')


