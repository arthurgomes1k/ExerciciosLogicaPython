dis = float(input('Qual a distancia da viagem? '))
if dis > 200:
    print(f'Na sua viagem de {dis} Km foi cobrado um valor de {dis * 0.45:.2f} R$')
else:
    print(f'Na sua viagem de {dis} Km foi cobrado um valor de {dis * 0.50:.2f} R$')
