nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[7mA primeira NOTA sendo {}, e a SEGUNDA sendo {}, a média do aluno será {}\033[m'.format(nota1, nota2, media))

if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')

