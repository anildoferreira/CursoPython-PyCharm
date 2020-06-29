salario = float(input('Digite o valor seu salário: '))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 / 100)
print('Seu novo salário é de: {:.2f}'.format(salario))


