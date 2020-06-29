totalMulheresMenor20 = 0
totalHomens = 0
totalPessoasMaior18 = 0
while True:
    idade = int(input('Qual a sua idade: '))
    if idade >= 18:
        totalPessoasMaior18 += 1

    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Qual o seu sexo? [F/M]: ')).strip().lower()[0]
        if sexo == 'f':
            if idade < 20:
                totalMulheresMenor20 += 1
        elif sexo == 'm':
            totalHomens += 1

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('acabou')
print(f'Acima de 18 anos, existem {totalPessoasMaior18} pessoas')
print(f'Homens cadastrados foram {totalHomens}')
print(f'Mulheres menor de 20 foram {totalMulheresMenor20}')