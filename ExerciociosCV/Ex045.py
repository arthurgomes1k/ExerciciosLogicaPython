from random import randint
from time import sleep

print('''Escolha um opção:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
player = int(input('Qual a sua jogada? '))
pc = randint(1, 3)
sleep(0.5)
print('JO')
sleep(0.75)
print('KEN')
sleep(1)
print('PO!!!')
print('\/ ' * 6)

if player == 1 and pc == 1:
    print('Joguei Pedra!')
    print('Empatou!')
elif player == 1 and pc == 2:
    print('Joguei Papel!')
    print('Você perdeu!')
elif player == 1 and pc == 3:
    print('Joguei Tesoura!')
    print('Você venceu!')
elif player == 2 and pc == 1:
    print('Joguei Pedra!')
    print('Você venceu')
elif player == 2 and pc == 2:
    print('Joguei Papel!')
    print('Empatou!')
elif player == 2 and pc == 3:
    print('Joguei Tesoura!')
    print('Você perdeu!')
elif player == 3 and pc == 1:
    print('Joguei Pedra!')
    print('Você perdeu!')
elif player == 3 and pc == 2:
    print('Joguei Papel!')
    print('Você venceu')
elif player == 3 and pc == 3:
    print('Joguei Tesoura!')
    print('Empatou!')
else:
    print('Opção invalida.Tente novamente!')
print('/\ ' * 6)
