from random import randint
v = 0
while True:
    vc = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = vc + pc
    op = ' '
    while op not in 'pi':
        op = str(input('Par ou ímpar? [P/I]')).lower().strip()[0]
    print(f'Você jogou {vc} e o computador jogou {pc} e o total foi {total}', end=' >>>')
    print('Deu PAR' if 0 == total % 2 else 'deu ÍMPAR')
    if op == 'p':
        if 0 == total % 2:
            print('Você ganhou')
            v += 1
        else:
            print('Você perdeu')
            break
    elif op == 'i':
        if 1 == total % 2:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('vamos jogar novamente!')
print(f'GAME OVER, vc venceu {v} x')




