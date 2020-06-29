temp = []
princ = []
c = maior = menor = 0
continuar = ' '
while continuar not in 'Nn':
    c += 1
    print(f'{c}º PESSOA')
    print('-' * 10)
    temp.append(str(input(f'Digite o seu nome: ')))
    temp.append(float(input(f'Digite o seu peso: ')))
    if c == 1:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]:'))
        if continuar in 'NnSs':
            break
        print('Tente novamente!', end=' ')
print(f'Foram cadastradas {c} pessoas.')
print(f'O maior peso foi de {maior}',end=' ')
for p in princ:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi de {menor}',end=' ')
for p in princ:
    if p[1] == menor:
        print(p[0])





