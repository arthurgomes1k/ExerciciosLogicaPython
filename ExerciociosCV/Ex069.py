print('-='*12)
print('CADASTRO DE USUÁRIO')
print('-='*12)

total18 = 0
homens = 0
mulheres20 = 0

verdadeiro = True

while verdadeiro:

    print('~' * 30)
    print('INFORME OS DADOS:')
    print('~' * 30)

    idade = int(input('Idade: '))
    while True:
        sexo = input('Sexo [ M / F ]: ').strip().lower()
        if sexo in 'mf':
            break

    if idade > 18:
        total18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres20 += 1

    print('~' * 30)

    while True:
        continuar = input('Quer continuar [S/N]: ').strip().lower()
        if continuar == 's':
            break
        elif continuar == 'n':
            verdadeiro = False
            break
print(' ')
print('====== Fim Do Programa ======')
print(f'Total de pessoal com mais de 18 anos: {total18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres20} mulheres com menos de 20 anos')
