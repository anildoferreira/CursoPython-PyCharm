a = [2, 5, 5, 5]
b = a
print(f'lista A: {a}')
print(f'Lista B: {b}')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

num = [2, 9, 3, 1]
num[0] = 7
num.append(4)
num.insert(3, 1)
num.pop()
num.remove(9)
if 3 in num:
    num.remove(3)
print(num)
print(f'essa lista tem {len(num)} elementos')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o  valor: {v}')
print('Cheguei ao final da lista')
for c, v in enumerate(valores):
    print(f'{c} and {v}')