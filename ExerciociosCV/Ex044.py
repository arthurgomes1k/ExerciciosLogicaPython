preço = float(input('Valor do produto: '))
print('=' * 20, 'Supermercado Do Arthur', '=' * 20)
print('''Como deseja realizar o pagamento?
[ 1 ] A vista em dinheiro com 10% de desconto
[ 2 ] A vista no cartão com 5% de desconto
[ 3 ] Em 2x sem juros no cartão
[ 4 ] Em 3x ou mais no cartão com 20% de juros''')
opção = int(input('Sua escolha: '))

if opção == 1:
    print(f'O produto de preço R${preço:.2f} fica de R${preço - preço * 0.10:.2f} a vista em dinheiro.')
elif opção == 2:
    print(f'O produto de preço R${preço:.2f} fica de R${preço - preço * 0.05:.2f} a vista no cartão.')
elif opção == 3:
    print(f'Não a alteração no preço o produto fica por R${preço:.2f} em 2x de R${preço / 2:.2f}')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'O produto de preço R${preço:.2f} fica de R${preço + preço * 0.20:.2f} em {parcelas}x ')
else:
    print('Opção inválida, tente novamente.')
