from datetime import date
ano = int(input('Digite o ano para saber se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:
    print('Sim, o ano de {} é bissexto'.format(ano))
else:
    print('Náo, o ano de {} não é bissexto'.format(ano))
