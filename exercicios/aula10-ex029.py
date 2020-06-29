velocidade = float(input('Lendo a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado')
    limite = 80
    multa = (velocidade - limite)
    valorMulta = 7 * multa
    print('O valor da sua multa é de {}'.format(valorMulta))
print('Dirija com segurança!')
