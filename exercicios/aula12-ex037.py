import math

num= int(input('\033[7mDigite qual o número para conversão:\033[m'))
print('''Escolha qual a conversao desejada.'
[ 1 ] converter pa BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O número {}, convertido para BINÁRIO será {}'.format(num, bin(num)[:2]))
elif opcao == 2:
    print('O número {}, convertido para OCTAL será {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {}, convertido para HEXADECIMAL será {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')




