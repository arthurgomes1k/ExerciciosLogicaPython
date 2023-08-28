from time import sleep


contador = 0
total_idade = 0
maior = 0
nome_maior = 'Nunhum'
contador_fem = 0

for x in range(1, 5):
    print(f'----- {x}ª PESSOA -----')
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    sexo = input('Sexo digite "M" ou "F": ')

    total_idade += idade
    contador += 1
    media = total_idade / contador

    if sexo.lower() == 'm':
        if idade > maior:
            maior = idade
            nome_maior = nome
    if sexo.lower() == 'f':
        if idade < 20:
            contador_fem += 1

print('Analisando')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print(f'A média de idade do grupo é "{media:.1f}"')
print(f'{nome_maior} Tem {maior} anos e é o homem que tem a maior idade')
print(f'{contador_fem} mulheres tem menos que 20 anos')
