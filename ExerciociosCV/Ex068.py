from random import randint

print('~' * 40)
print('VAMOS TIRAR NO PAR OU IMPAR')
print('~' * 40)

Vitorias = 0

while True:

    while True:
        escolha = input('Escolha "Impar" ou "Par": ').strip().lower()
        if escolha == 'par':
            escolhapc = 'impar'
        elif escolha == 'impar':
            escolhapc = 'par'
        if escolha == 'impar' or escolha == 'par':
            break

    num = int(input('Escolha um número: '))
    numpc = randint(1, 10)
    total = num + numpc

    print('~' * 40)
    if total % 2 == 0:
        if escolhapc == 'par' and escolha == 'impar':
            print(f'Você jogou {num} computador jogou {numpc}, total de {total} deu PAR')
            print('Você PERDEU!')
            break
        elif escolhapc == 'impar' and escolha == 'par':
            print(f'Você jogou {num} computador jogou {numpc}, total de {total} deu PAR')
            print('Você VENCEU!')
            print('Vamos de novo...')
            Vitorias += 1


    if total % 2 == 1:
        if escolhapc == 'par' and escolha == 'impar':
            print(f'Você jogou {num} computador jogou {numpc}, total de {total} deu IMPAR')
            print('Você VENCEU!')
            print('Vamos de novo...')
            Vitorias += 1
        elif escolhapc == 'impar' and escolha == 'par':
            print(f'Você jogou {num} computador jogou {numpc}, total de {total} deu IMPAR')
            print('Você PERDEU!')
            break
    print('~' * 40)

print(f'GAME OVER! você venceu {Vitorias} vezes.')
