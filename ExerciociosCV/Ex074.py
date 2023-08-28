from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valoers foram {numeros}')
num_em_ordem = sorted(numeros)
print(f'O maior valor sorteado foi {num_em_ordem[4]}')
print(f'O menor valor sorteado foi {num_em_ordem[0]}')
