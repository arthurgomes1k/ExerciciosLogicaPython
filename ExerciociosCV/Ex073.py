times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Curitiba', 'Avaí', 'Ponte preta', 'Atlético-GO')

print('~~' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('~~' * 20)
print(f'Os 4 últimos são: {times[-1:-5:-1]}')
print('~~' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('~~' * 20)
# print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição.')
for c in range(0, len(times)):
    if (times[c]) == 'Chapecoense':
        print(f'O chapecoense está na {c + 1}ª posição')
print('~~' * 20)
