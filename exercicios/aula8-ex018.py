import math
ang = float(input('Digite o valor do seu angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sen, cos, tan))


