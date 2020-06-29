times = 'Atlético', 'Botafogo', 'Cruzeiro', 'Democrata', 'Estanciano', 'Flamengo', 'Grêmio', 'Horizonte', 'Internacional', 'Juventude', 'Kapital', 'Luverdense', 'Mixto', 'Náutico', 'Operário', 'Palmeiras', 'Quissamã', 'Remo', 'São Paulo', 'Tupi', 'Uberaba', 'Vasco da Gama', 'Wenceslauense', 'Xanxerense', 'Ypiranga', 'Zumbi'
print('-=' * 30)
print(f'LISTA DE TIMES DO BRASILEIRÃO: {times}')
print('-=' * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os últimos 4 colocados são : {times[-4:]}')
print(f'Os times em ordem alfabética são : {sorted(times)}')
print(f'O Horizonte está na {times.index("Horizonte")+1}ª posição')
