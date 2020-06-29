from datetime import date
atual = date.today().year
countMaior = 0
countMenor = 0

for c in range(1, 8):
    nasc = int(input('\033[7mEm que ano a {}ª pessoa nasceu?\033[m '.format(c)))
    idade = atual - nasc

    if idade >= 18:
        countMaior += 1
        print('você é maior de idade!')
    else:
        countMenor += 1
        print('Você é menor de idade')
print('{} maiores de idade\n{} menores de idade'.format(countMaior, countMenor))
