a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))

tupla = a, b, c, d

print(f'Os números digitados foram {tupla}')

quantos9 = 0
for n in tupla:
    if n == 9:
        quantos9 += 1
print(f'O número 9 apareceu {quantos9} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu em nenhuma das posições')

'''if a == 3:
    posi = 1
    print(f'O número 3 apareceu na {posi}° posição')
elif b == 3:
    posi = 2
    print(f'O número 3 apareceu na {posi}° posição')
elif c == 3:
    posi = 3
    print(f'O número 3 apareceu na {posi}° posição')
elif d == 3:
    posi = 4
    print(f'O número 3 apareceu na {posi}° posição')
else:
    print('O número 3 não apareceu em nenhuma das posições')'''

print(f'Os valores pares digitados foram', end=' ')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')
