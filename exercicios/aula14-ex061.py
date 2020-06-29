'''n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
for c in range(n, 50, r):
    print(c, end=' → ')
print('FIM')'''

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c = 1
while c <= 10:
    c += 1
    n += r
    print(n, end=' → ')
print('FIM')

