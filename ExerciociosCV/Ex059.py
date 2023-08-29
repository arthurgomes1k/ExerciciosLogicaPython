from time import sleep
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:
    print('O que você deseja fazer?\nDigite o número correspondente para fazer sua escolha: ')
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior número')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        print(f'{v1} + {v2} = {v1 + v2}')
    elif escolha == 2:
        print(f'{v1} x {v2} = {v1 * v2}')
    elif escolha == 3:
        if v1 > v2:
            print(f'{v1} é maior que {v2}')
        elif v1 < v2:
            print(f'{v2} é maior que {v1}')
        elif v1 == v2:
            print(f'Os dois valores são iguais!')
    elif escolha == 4:
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Obrigado pela preferencia!:)')
    else:
        print('Opção invalida, tente novamente.')
    print('-'*30)
    sleep(2)
