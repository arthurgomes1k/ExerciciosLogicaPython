n = 0
contador = 0
soma = 0

while True:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    contador += 1
    soma += n

print(f'Você digitou {contador} número(s)')
print(f'E a soma entre eles é {soma}!')
