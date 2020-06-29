l = []
for c in range(1, 6):
    n = int(input(f'Digite o {c} número: '))
    if c == 1 or n >= l[-1]:
        l.append(n)
    else:
        for v in l:
            if v >= n:
                l.insert(l.index(v), n)
                break
print(l)












