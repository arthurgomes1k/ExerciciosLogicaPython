from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano

print('Qual seu sexo?\n'
      'Digite [ M ] para masculino.\n'
      'Digite [ F ] para feminino.')
sexo = input('Sua escolha: ')

if sexo.upper() == 'F':
    print('Você não precisa fazer alistamento obrigatorio!')

if sexo.upper() == 'M':
    if idade < 18:
        print(f'Ainda não esta na hora de você se alistar, faltam {18 - idade} ano(s)')
        print(f'Seu alistamento será em {(18 - idade) + atual}')

    elif idade == 18:
        print('Você tem 18 anos e está na hora de você se alistar')

    elif idade > 18:
        print(f'Já passou da hora de você se alisar, passou {idade - 18} ano(s) do seu alistamento')
        print(f'Seu alistamento foi em {atual - (idade - 18)}')

else:
    print('Digito invalido!')
