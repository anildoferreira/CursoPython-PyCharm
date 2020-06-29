lista = []
listaPar = []
listaImpar = []
continuar = ' '
c = n = 0
while continuar not in 'Nn':
    c += 1
    n = int(input(f'Digite o {c}º número: '))
    lista.append(n)
    if 0 == n % 2:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip()[0]
        if continuar in 'NnSs':
            break
        print('Tente novamente!', end=' ')
print('-=' * 15)
print(f'Lista COMPLETA: {lista}')
print(f'Lista PAR: {listaPar}')
print(f'Lista ÍMPAR: {listaImpar}')
