print('-='*18+'-')
print('        Supermercado Arthur      ')
print('-='*18+'-')

total = mais1000 = menor = nome_do_menor = cont = 0

verdadeiro = True

while verdadeiro:

    cont += 1
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))

    total += preco
    if cont == 1:
        menor = preco
    if preco > 1000:
        mais1000 += 1
    if preco < menor:
        menor = preco
        nome_do_menor = produto

    while True:
        continuar = input('Quer continuar [S/N]: ').strip().lower()
        if continuar == 's':
            break
        elif continuar == 'n':
            verdadeiro = False
            break

print(' ')
print('====== Fim Do Programa ======')
print(f'O total da compra foi {total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_do_menor} que custa R${menor:.2f}')
