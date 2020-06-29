nome = str(input('Digite o seu nome: '))
if nome == 'ANILDO':
    print('Eu te encontrei :)')
elif nome in 'Pedro Paulo Bruno':
    print('Seu nome é bem popular!')
else:
    print("{}, não é quem eu estou procurando!".format(nome))
