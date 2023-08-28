peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

print(f'Seu IMC é {imc:.2f} e você está ', end='')
if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 <= imc < 25:
    print('com peso ideal.')
elif 25 <= imc < 30:
    print('com sobrepeso.')
elif 30 <= imc < 40:
    print('com obesidade.')
elif imc >= 40:
    print('com obesidade mórbida.')
