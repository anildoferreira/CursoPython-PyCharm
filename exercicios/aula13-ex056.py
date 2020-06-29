mediaIdade = 0
homemVelho = ''
idadeVelho = 0
somaIdade = 0
mediaIdade = 0
mulherMenor = 0
for p in range(1, 5):
    print('-----{}ª PESSOA-----'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaIdade += idade
    if p == 1:
        if sexo == 'm':
            homemVelho = nome
            idadeVelho = idade
    if sexo == 'm':
        if idade > idadeVelho:
            homemVelho = nome
            idadeVelho = idade
    else:
        if sexo == 'f':
            if idade < 20:
                mulherMenor += 1

mediaIdade = somaIdade / 4
print('A idade média do grupo é de {} anos".format(mediaIdade')
print('O homem mais velho tem {} e se chama {}'.format(idadeVelho, homemVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulherMenor))


