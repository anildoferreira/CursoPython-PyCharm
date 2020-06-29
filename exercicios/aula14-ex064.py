soma = 0
c = 0
n = 0
while n != 999:
    n = int(input('Digite seu número para soma: '))
    if n != 999:
        c = c + 1
        soma += n
print('Foram {} digitados e a soma é {}'.format(c, soma))

