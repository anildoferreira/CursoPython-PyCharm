import math
print('-=' * 22)
print('CALCULANDO SOMA E ECONTRANDO MÚLTIPLOS DE 3')
print('-=' * 22)
soma = 0
contador = 0
for impar in range(1, 500, 2):
    if 0 == impar % 3:
        soma += impar
        contador += 1
print('A soma dos números divisíveis por 3 é {}'.format(soma))
print('A quantidade de múltiplos por 3 é {}'.format(contador))

