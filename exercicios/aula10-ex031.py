distancia = float(input('Qual a distância da sua viagem? '))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''if distancia <= 200:
    print('O valor da sua passagem é de R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor da sua passagem é de R${:.2f}'.format(distancia * 0.45))'''
print('O valor da sua passagem é de R${}'.format(preco))
print('Tenha uma boa viagem!')
