num = (int(input(f'Digite o primeiro número: ')),
       int(input(f'Digite o segundo número: ')),
       int(input(f'Digite o terceiro número: ')),
       int(input(f'Digite o quarto número: ')))
print(f'Você digitou os valores {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado!')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}.')
else:
    print('O valor 3 não foi digitado!')
print(f'Os números pares digitados foram: ', end='')
for par in num:
    if 0 == par % 2:
        print(par, end=' ')
