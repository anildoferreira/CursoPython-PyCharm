contador = soma = media = maior = menor = 0
r = ''
while r != 'n':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if r not in 's or n':
        print('Opção incorreta, tente novamente!')
    contador += 1
    soma += n
    media = soma / contador
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {} '.format(contador, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


