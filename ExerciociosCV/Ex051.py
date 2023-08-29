pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termo10 = pt + 10 * r

if r == 0:
    for x in range(0, 10):
        print(pt, end=' > ')
else:
    for x in range(pt, termo10, r):
        print(x, end=' > ')
print('Fim')
