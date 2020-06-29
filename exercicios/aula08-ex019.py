from random import choice
n1 = str(input('Digite o primeiro nome para o soteio: '))
n2 = str(input('Digite o segundo nome para o sorteio: '))
n3 = str(input('Digite o terceiro nome para o sorteio: '))
n4 = str(input('Digite o quarto nome para o sorteio: '))
lista = [n1, n2, n3, n4]
escolha = choice(lista)
print('O escolhido foi: {}'.format(escolha))
