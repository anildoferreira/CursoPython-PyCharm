while True:
    n = int(input('Digite um número para tabuada: '))
    if n < 0:
        break
    for c in range(1, 11, 1):
        t = n * c
        print(f'{n} x {c} = {t}')
print('Programa tabuada encerrado, volte sempre!')