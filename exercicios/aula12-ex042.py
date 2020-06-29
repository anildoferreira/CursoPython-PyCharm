r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

#Determinado se é possível a formação de um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim, será possível formar um triângulo! ', end='')
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    elif r1 != r2 != r3 !=r1:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('Não será possível formar um triângulo!')



