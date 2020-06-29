rep = ' '
c = 0
l = list()
while rep not in 'Nn':
    c += 1
    l.append(int(input(f'Digite o {c}° número: ')))
    while True:
        rep = str(input('Quer continuar? [S/N]: ')).strip()[0]
        if rep in 'NnSs':
            break
        print('Tente novamente!', end=' ')
print(f'Foram Digitados {c} números.')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
if 5 in l:
    print('Sim, contém o valor 5 na lista!')
else:
    print('Não contém o valor 5 na lista!')



