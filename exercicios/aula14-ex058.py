from random import randint
computador = randint(0,10)
print('Sou o COMPUTADOR, tente acertar o núemro q eu estou pensado de 1 a 10')

acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite qual é o seu palipite: '))
    palpite +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('pra cima')
        elif jogador > computador:
            print('pra baixo')
print('Ganhou com {} palpites'.format(palpite))
