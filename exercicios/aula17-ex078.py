valores = list()
maior = menor = 0
i = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c} valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O valor máximo na lista foi de {maior} na posição', end=' ')

for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i+1}...', end='')
print()
print(f'O valor mínimo na lista foi de {menor} na posição', end=' ')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i+1}...', end='')





