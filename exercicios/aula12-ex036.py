print('-=' * 27)
print('Responda as perguntas a seguir para financiar sua casa'.upper())
print('-=' * 27)

# Variáveis
valorImovel = float(input('Digite o valor do imóvel: '))
meses = float(input('Digite quantos meses de financiamento: '))
salario = float(input('Digite o valor do seu salário: '))

# Condições
parcelas = valorImovel / meses
salarioPotencial = salario * (30 / 100)

print('\33[7;32mSalário potencial R${:.2f}\033[m'.format(salarioPotencial))
print('\033[7;31mvalor das parcelas {:.2f}\033[m'.format(parcelas))

if parcelas >= salarioPotencial:
    print('APROVADO')
else:
    print('NEGADO')
