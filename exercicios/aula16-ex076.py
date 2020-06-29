listagem = ('Borracha', 1.75,
            'Lápis', 1.00,
            'Caderno', 10.00,
            'Apontador', 2.00,
            'Estojo', 5.00,
            'Caneta', 2.50,
            'Livros', 99.00)

print('-=' * 20)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-=' * 20)
for pos in range(0, len(listagem)):
    if 0 == pos % 2:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {listagem[pos]:>6.2f}')
print('-=' * 20)