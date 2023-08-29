sexo = str(input('Digite seu sexo "M" ou "F": ')).strip().lower()
while sexo not in ['m', 'f']:
    sexo = str(input('Dados inválidos. Por favor digite seu sexo "M" ou "F": ')).strip().lower()
print('Sexo registrado com sucesso')
