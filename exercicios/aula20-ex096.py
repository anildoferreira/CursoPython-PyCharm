def area(larg, compr):
    a = larg * compr
    print(f'A área de um terreno {larg} x {compr} é de {a} m².')


# Programa Principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comptimento (m): '))
area(l, c)
