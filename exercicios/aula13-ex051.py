print('-=' * 10)
print('10 TERMOS DE UMA PA')
print('-=' * 10)

termo = int(input('Dgite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for pa in range(termo, 10, razao):
    print('{}'.format(pa), end=' -> ')
print()