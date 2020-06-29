frase = str(input('Digite uma frase: ')).strip().upper()
palavrasSeparadas = frase.split()
junto = ''.join(palavrasSeparadas)
inverso = junto[::-1]

print(junto, inverso)
if junto == inverso:
    print('Sim, é um palíndromo')
else:
    print('Não é um palíndromo')



