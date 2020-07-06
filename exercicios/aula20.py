'''def linha():
    print('-------------')

linha()
print('Curso em vídeo')
linha()

def título(msg):
    print('-------------')
    print(msg)
    print('-------------')


título('Testando Função!')
título('Outra teste')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# Programa Principal
soma(4, 5)
soma(2, 9)
soma(3, 8)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores de num {num} e o seu tamanho é de {tam}')


contador(2, 3, 5, 0, 4)
contador(4, 5, 4, 9)
contador(3, 5, 7)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [2, 5, 6, 4]
dobra(valores)
print(valores)'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {num}, a soma é {s}')


soma(2, 5, 5)
soma(2, 4)


