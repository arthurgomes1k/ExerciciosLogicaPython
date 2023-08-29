n = int(input('Digite um número para ver seu fatorial: '))
print(f'{n}! = {n} x ', end='')

for x in range(n-1, 1, -1):
    if x == (n-1):
        print(f'{x} x ', end='')
        total = n * x
    else:
        print(f'{x} x ', end='')
        total = total * x
print(f'{x-1} = {total}')



n = int(input('Digite um número para ver seu fatorial: '))
contador = n - 1
print(f'{n}! = {n} x ', end='')
total = n * contador

while contador >= 2:
    print(f'{contador} x ', end='')
    contador -= 1
    total *= contador
print(f'{contador} = {total}')
