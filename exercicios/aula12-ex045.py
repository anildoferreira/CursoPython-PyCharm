from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções de jogo
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

vc = int(input('Digite sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-='* 10)
print('O pc escolheu {}'.format(itens[pc]))
print('Você escolheu {}'.format(itens[vc]))
print('-='* 10)

if pc == 0 and vc == 1 or pc == 1 and vc == 2 or pc == 2 and vc == 0:
    print('GANHOU')
elif pc == 0 and vc == 0 or pc == 1 and vc == 1 or pc == 2 and vc == 2:
    print('EMPATOU')
else:
    print('PERDEU')

