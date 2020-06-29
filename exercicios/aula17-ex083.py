pilha = []
exp = str(input('Digite a expressão: '))
for parenteses in exp:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
            break
print('_' * 30)
if len(pilha) == 0:
    print('Expressão VÁLIDA!')
else:
    print('Expressão INVÁLIDA!')







