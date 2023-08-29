pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
contador = 0

while contador < 10:
    print(f'{pt} > ', end='')
    pt += r
    contador += 1
print('Fim')
