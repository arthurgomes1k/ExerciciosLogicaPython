n = int(input('Digite um número: '))
s = 0

if n >= 2:
    for x in range(2, n):
        if n % x == 0:
            s = s + 1
    if s == 0:
        print(f'O número {n} é primo!')
    elif s != 0:
        print(f'O número {n} não é primo!')
elif n == 1:
    print(f'O número {n} não é primo!')
else:
    print(f'O número {n} é negativo ou neutro!')