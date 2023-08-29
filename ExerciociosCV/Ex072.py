extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorse',
           'quinse', 'deseseis', 'desesete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou {extenso[numero]}')

        while 0 <= numero <= 20:
            continuar = input('Quer continuar [S/N]? ').strip().upper()
            if continuar in 'SN':
                break
        if continuar == 'N':
            break
    if continuar != 'S':
        print('Tente novamente,', end=' ')
    continuar = ' '

print('Thanks')
