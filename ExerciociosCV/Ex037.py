n = int(input('Digite um número:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converte epara BINÁRIO')
print('[ 2 ] converte epara OCTAL')
print('[ 3 ] converte epara HEXADECIMAL')
b = int(input('Sua opção: '))

'''if b == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif b == 2:
    print(f'{n} convertido em OCTAL é igual a {oct(n)[2:]}')
elif b == 3:
    print(f'{n} convertido em hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida!')'''

if b == 1:
    print(f'{n} convertido para BINÁRIO é igual a {n:b}')
elif b == 2:
    print(f'{n} convertido em OCTAL é igual a {n:o}')
elif b == 3:
    print(f'{n} convertido em hexadecimal é igual a {n:X}')
else:
    print('Opção inválida!')
