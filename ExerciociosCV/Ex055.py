maior = 0
menor = 0

for x in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if x == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')