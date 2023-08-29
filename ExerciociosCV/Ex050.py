s = 0
contador = 0
for x in range(1, 7):
    n = int(input(f'Digite o {x}º número: '))
    if n % 2 == 0:
        s = n + s
        contador += 1
print(f'A soma dos {contador} números pares é {s}')