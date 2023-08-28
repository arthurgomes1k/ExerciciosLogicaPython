v = int(input('Velocidade registrada: '))
if v > 80:
    print(f'Você ultrapassou o limite de velocidade. \n'
          f'E sua multa é de {(v - 80)*7:.2f} R$')
else:
    print('Você passou dentro do limite de volocidade permitido!')
