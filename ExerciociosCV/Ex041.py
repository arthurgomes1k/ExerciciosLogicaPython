from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano

print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Mirim')

elif 9 < idade <= 14:
    print('Infantil')

elif 14 < idade <= 19:
    print('Junior')

elif 19 < idade <= 20:
    print('Sênior')

else:
    print('Master')
