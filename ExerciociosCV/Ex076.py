listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

produto = 0
preco = 1

while preco < 18:
    print(f'{listagem[produto]:.<30}R${listagem[preco]:>7.2f}')
    produto += 2
    preco += 2
print('-'*40)
