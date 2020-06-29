n = int(input('Digite seu número para sequência de FIBONACCI: '))
n1 = 0
n2 = 1
n3 = n1 + n2
print('{} → {} → {}'.format(n1, n2, n3), end='')
c = 4
while c <= n:
    c = c + 1
    n4 = n2 + n3
    n2 = n3
    n3 = n4
    print(' → {}'.format(n4), end='')
print(' → FIM')
