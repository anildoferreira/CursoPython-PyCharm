extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
          'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

loop = ' '
while loop not in 'n':
    while True:
        num = int(input('Digite um número: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente!', end=' ')
    print(f'Vc digitou o número {extenso[num]}')
    while True:
        loop = str(input('Quer continuar? [S/N]: ')).strip().lower()
        if loop in 'ns':
            break
        print('Tente novamente!', end=' ')
print('fim')













