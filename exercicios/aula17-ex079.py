lista = []
cont = ' '
while cont not in 'Nn':
    n = int(input('Digite um valor para a lista: '))
    if n not in lista:
        lista.append(n)
        print(f'O valor {n} foi adicionado com sucesso!')
    else:
        print(f'O valor {n} já foi adicionado, tente novamente!')
    while True:
        cont = str(input('Quer continuar? [S/N]: ')).strip()[0]
        if cont in 'NnSs':
            break
        print('Tente novamente', end=' ')
print('-=' * 20)
print(f'Aqui estão os valores digitados da sua lista > {sorted(lista)}')




