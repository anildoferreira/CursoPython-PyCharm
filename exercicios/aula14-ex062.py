n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
c1 = 1
n2 = 10
tn = 0
while n2 != 0:
    tn = tn + n2
    while c1 <= tn:
        c1 += 1
        n1 += r
        print(n1, end=' → ')
    print('FIM')
    n2 = int(input('Digite mais quantos termos: '))
print('Progressão finalizada com {} termos mostrados.'.format(tn))
