from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até o {f} de {p} até {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('fim')
        print('-' * 40)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p
        print('fim')
        print('-' * 40)


# Programa Principal
contador(1, 10, 1)
contador(10, 1, 1)
print('Agora é a sua vez de inicializar a contagem!')
ini = int(input('Início : '))
fim = int(input('Fim    : '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
