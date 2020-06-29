r1 = float(input('Digite a primeira parte do triângulo: '))
r2 = float(input('Digite a segunda parte do triângulo: '))
r3 = float(input('Digite a terceira parte do triângulo: '))
print('-==' * 7)
print('ANALISANDO SE FORMAR UM TRIÂNGULO...')
print('-==' * 12)
# Descobrindo se a soma de uma variável é menor q somas das outras duas
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\33[32mSim, pode se formar um triângulo!')
else:
    print('\33[31mNão, pode se formar um triângulo!')



