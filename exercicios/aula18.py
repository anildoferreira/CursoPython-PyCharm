'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Joao', 22], ['Joaquim', 30], ['Bruno', 44], ['sebastiao', 80]]
print(galera[3][0])
for e, p in enumerate(galera):
    print(f'Na posição {e+1}, seu nome é: {p[0]}, com {p[1]} anos de idade.')'''

galera = []
dado = []
totMaior = totMenor = 0
for c in range(0, 3):
    galera.append(str(input('Digite o seu nome: ')))
    galera.append(float(input('Digite a sua idade: ')))
    dado.append(galera[:])
    galera.clear()
for p in dado:
    if p[1] >= 21:
        totMaior += 1
        print(f'A {p[0]} é maior de idade')
    else:
        totMenor += 1
        print(f'A {p[0]} é menor de idade')
print(f'Temos {totMaior} maior de idade e {totMenor} de idade no TOTAL.')
