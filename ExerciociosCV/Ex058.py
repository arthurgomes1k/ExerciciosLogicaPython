from random import randint

print('Tente Adivinhar o número que eu estou pensado.')
play = int(input('Pense em um número entre 0 e 10: '))
pc = randint(0, 10)
contador = 1

while play != pc:
    if 0 <= play <= 10:
        while play != pc:
            if play != pc:
                contador += 1
                if play > pc:
                    play = int(input('Menos... \nPense em outro número entre 0 e 10: '))
                if pc > play:
                    play = int(input('Mais... \nPense em outro número entre 0 e 10: '))
        else:
            print(f'Parabens você acertou depois de {contador} tentativas, pensei no número {pc}!')
    else:
        play = int(input('Digito invalido, digite um número entre 0 e 10: '))
        contador += 1
if contador == 1:
    print(f'Parabens você acertou de primeira!!!! pensei no número {pc}!')