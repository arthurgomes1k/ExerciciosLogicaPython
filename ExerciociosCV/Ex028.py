from random import randint
play = int(input('Pense em um número entre 0 e 5: '))
pc = randint(0, 5)
if play == pc:
    print('Parabéns você acertou!')
else:
    print(f'Que pena você errou, pensei no número {pc}!')
