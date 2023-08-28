n = input('Digite um número: ')
contador = 0
soma = 0
maior = int(n)
menor = int(n)

while n != 'fim':
    contador += 1
    soma += int(n)
    if int(n) > maior:
        maior = int(n)
    if int(n) < menor:
        menor = int(n)
    n = input('Digite um número, ou digite "Fim" para parar: ')

print(f'A media dos números é {soma / contador}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
