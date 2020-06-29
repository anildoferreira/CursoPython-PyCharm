from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#print(f'Os valores sorteados foram: {n}')
print(f'Os valores sorteados foram: ', end='')
for cont in n:
    print(f'{cont}', end=', ')
print(f'\nO maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
