print('-' * 40)
valor = int(input('Quer ver a tabuada de qual valor? '))
contador = 1
print('-' * 40)

while True:
    print(f'{valor} x {contador} = {valor * contador}')
    contador += 1
    if contador > 10:
        print('-' * 40)
        valor = int(input('Quer ver a tabuada de qual valor? '))
        print('-' * 40)
        contador = 1
        if valor < 0:
            print('Programa da tabuada encerrado, volte sempre!')
            break