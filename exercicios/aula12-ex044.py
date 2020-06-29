print('{:=^40}'.format('FORMAS DE PAGAMENTO'))
preco = float(input('Digite o valor das compras: '))
print('''ESCOLHA SUA OPÇÃO DE PAGAMENTO
[ 1 ] Dinheiro 10% DESCONTO
[ 2 ] Débito 5% DESCONTO
[ 3 ] Cartão 2x SEM DESCONTO
[ 4 ] Cartão 3x acima 20% JUROS''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    desconto = preco * 0.90
    print('Sua compra de R${:.2f} menos 10% desc. no Dinheiro = R${}'.format(preco, desconto))
elif opcao == 2:
    desconto = preco * 0.95
    print('Sua compra de R${:.2f} menos 5% desc. no Débito = R${}'.format(preco, desconto))
elif opcao == 3:
    print('Sua compras de R${:.2f}, parcelado em 2x sem juros.'.format(preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    acrescimo = preco * 1.20
    print('Sua compra de R${:.2f} parcelado em {}x com juros de 20% no cartão = R${}'.format(preco, parcelas, acrescimo))




