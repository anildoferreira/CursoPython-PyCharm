contador = 1
totalCompra = 0
produtoAcima1000 = 0
menorPreco = 0
produtoMaisBarato = 0
while True:
    produto = str(input(f'Digite o {contador} produto: '))
    contador += 1
    preco = float(input('Digite o preço: R$ '))
    totalCompra += preco
    if preco > 1000:
        produtoAcima1000 += 1
    if contador == 2 or preco < menorPreco:
        menorPreco = preco
        produtoMaisBarato = produto
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total da compra foi {totalCompra:.2f}')
print(f'Produto acima de R$ 1000 foi {produtoAcima1000}')
print(f'O {produtoMaisBarato} mais barato custa {menorPreco:.2f}')