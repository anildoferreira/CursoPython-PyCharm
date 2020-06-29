'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''r = 's'
while r == 's':
    n = int(input('Digite  número: '))
    r = str(input('Quer continuar [S/N]? ')).strip().lower()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if 0 == n % 2:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
