matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mlin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]',end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol} ')
for c in range(0, 3):
    if c == 0:
        mlin = matriz[1][c]
    elif matriz[1][c] > mlin:
        mlin = matriz[1][c]
print(f'O maior valor da segunda linha é {mlin}')