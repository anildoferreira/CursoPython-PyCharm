from random import randint
from time import sleep
comp = randint(0, 5) # Faz o computador escolher o número
print('>$<' * 17)
print('Vou pensar em um número de (0 à 5), tente advinhar!')
print('>$<' * 17)
jogador = int(input('Digite aqui seu número da sorte: ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == comp:
    print('Você ganhouuuu!')
else:
    print('Eu pensei no {}'.format(comp),'tente novamente!')