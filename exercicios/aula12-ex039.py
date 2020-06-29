from datetime import date
anoAtual = date.today().year

sexo = int(input('''\033[7mQual o seu sexo: \033[m
[ 1 ] MASCULINO
[ 2 ] FEMININO'''))

if sexo == 2:
    print('Você não precisa se alistar!')

nasc = int(input('Digite o ano de seu nascimento: '))
idade = anoAtual - nasc
print('\033[7mQuem nasceu em {}, tem {} ano(s) em {}\033[m'.format(nasc, idade, anoAtual))

if idade < 18:
    tempo = 18 - idade
    prev = anoAtual + tempo
    print('Você deverá se alistar alistar daqui {} ano(s)'.format(tempo))
    print('Seu alistamento será em {}'.format(prev))
elif idade == 18:
    print('Você deve se alistar imediatamente!')
else:
    tempo = idade - 18
    prev = anoAtual - tempo
    print('\033[7;31mVocê já passou do tempo de alistamento a {} ano(s)\033[m'.format(tempo))
    print('Seu alistamento foi no ano de {}'.format(prev))





