from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 15)
print('{:-^30}'.format('JOGA NA LOTERIA'))
print('-=' * 15)
quant = int(input(f'Quanto jogos vc quer q eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    tot += 1
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-=' * 3, f'SORTEANDO {quant} DE JOGOS', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '=-' * 5)

