nome = str(input('Digite seu nome: '))
if nome == 'Arthur':
    print('que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é brm popular no brasil.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
