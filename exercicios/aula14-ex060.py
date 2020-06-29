'''n = int(input('Digite seu número fator: '))
c = n
f = 1
print('Calculando {} = '.format(n), end='')
while c > 1:
    c -= 1
    f *= c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)'''

'''from math import factorial
n = int(input('Digite um número para fatorar: '))
f = factorial(n)
print('o fator de {} é {}'.format(n, f))'''

m = 1
n = int(input('Digite seu número fator: '))
print('Fator de {} = '.format(n), end='')
for c in range(n, 0, -1):
    m *= c
    print(c, end='')
    print(' x 'if c > 1 else ' = ', end='')
print(m, end='')