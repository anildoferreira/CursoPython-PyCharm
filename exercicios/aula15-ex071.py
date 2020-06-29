total = int(input('Quanto vc quer sacar? R$ '))
nota = 50
totalNotas = 0
while True:
    if total >= nota:
        total -= nota
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f'Serão {totalNotas} de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalNotas = 0
        if total == 0:
            break










