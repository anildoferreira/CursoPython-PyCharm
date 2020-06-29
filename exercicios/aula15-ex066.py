contador = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Foram digitados {contador} valores, e a soma entre eles foi {soma}')
