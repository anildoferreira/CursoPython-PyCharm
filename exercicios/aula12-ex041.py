from datetime import date
anoAtual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - nasc
print('A sua idade é: {}'.format(idade))
if idade <= 9:
    print('Até 9 anos: MIRIM')
elif idade <= 14:
    print('Entre 9 e 14 anos: INFANTIL')
elif idade <= 19:
    print('Entre 15 e 19 anos: JUNIOR')
elif idade <= 25:
    print('Entre 20 e 25 anos: SÊNIOR')
elif idade <= 110:
    print('Acima: MASTER')
else:
    print('Idade inexistente')
