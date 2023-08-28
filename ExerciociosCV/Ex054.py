from datetime import date

demaior = 0
demenor = 0

for x in range(0, 7):
    y = int(input('Digite o ano de seu nascimento: '))
    z = date.today().year - y
    if z >= 21:
        demaior += 1
    elif z < 21:
        demenor += 1

print(f'{demaior} pessoa(s) aingiram a maioridade!')
print(f'{demenor} pessoa(s) ainda não aingiram a maioridade!')
