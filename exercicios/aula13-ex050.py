soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite {} inteiro: '.format(c)))
    if 0 == n % 2:
        soma += n
        cont += 1
print('você informou {} números PARES, e a soma foi {}'.format(cont, soma))
