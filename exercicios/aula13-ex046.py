from time import sleep
print('-=' * 15)
print('\033[7mCONTAGEM REGRESSIVA PARA FOGOS\033[m')
print('-=' * 15)

n = int(input('Digite um número de 1 à 10 para contagem Regressiva: '))
for c in range(n, -1, -1):
    print(c)
    sleep(1)
print('pow! pow!')

