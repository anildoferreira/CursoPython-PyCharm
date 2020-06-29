sexo = str(input('Digite seu sexo [M/F]: ')).strip()
while sexo not in 'FfMm':
    sexo = str(input('Opção inválida! Por favor informe seu sexo: ')).strip()
print('Sexo {} registrado com sucesso!'.format(sexo))

