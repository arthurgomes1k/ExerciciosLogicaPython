n = int(input('Digite um número: '))
print(f'A tabuada de {n} é:')
print('-' * 12)
for x in range(0, 11):
    t = n * x
    print(f'{n} x {x:2} = {t:2}')
print('-' * 12)
