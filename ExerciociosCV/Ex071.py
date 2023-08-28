print('='*28)
print('         BANCO ART      ')
print('='*28)

valor = int(input('Qual valor você quer sacar? R$'))
nota = 50
totalnotas = 0

'''contador = 0
while True:
    if contador == 1:
        nota = 20
    if contador == 2:
        nota = 10
    if contador == 3:
        nota = 1

    quantidade_notas = valor // nota
    resto = valor % nota
    valor = resto

    if quantidade_notas > 0:
        print(f'Total de {quantidade_notas} cédulas de R${nota}')

    contador += 1

    if contador == 4:
        break'''

while True:
    if valor >= nota:
        valor -= nota
        totalnotas += 1
    else:
        print(f'Total de {totalnotas} cédulas de R${nota}')
        totalnotas = 0
        if valor == 0:
            break
        elif valor < 10:
            nota = 1
        elif valor < 20:
            nota = 10
        elif valor < 50:
            nota = 20


print('='*28)
print('Volte sempre ao BANCO ART! Tenha um bom dia!')
