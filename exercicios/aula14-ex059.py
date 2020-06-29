opcao = 0
soma = 0
multi = 0
maior = 0
novosNum = 0
saiPro = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while opcao != 5:
    print('''Escolha uma opção abaixo
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('\033[7mQual é a sua opção?\033[m '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números é {}'.format(soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação é {}'.format(multi))
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
            print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('DIGITE NOVOS NÚMEROS...')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...!')
    else:
        print('Opção inválida! Digite novamente...')
    print('░' * 20)
print('FIM DO PROGRAMA, VOLTE SEMPRE!!!')

'''from time import sleep
for b in range(1,10):
    print('░', end='')
    sleep(1)'''

