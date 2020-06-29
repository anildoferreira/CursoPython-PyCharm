frase = str(input('Digite a sua frase: ')).strip().upper()
print('A letra (a) aparece {} vezes na sua frase'.format(frase.count('A')))
print('A letra (a) aparece na posição {}'.format(frase.find('A')+1))
print('A última letra aparece na posição {}'.format(frase.rfind('A')+1))
