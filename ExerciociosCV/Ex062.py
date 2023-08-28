pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
termos = 10
contador = 0

while contador < termos:
    print(f'{pt} > ', end='')
    pt += r
    contador += 1
    if contador == termos:
        termos = int(input('Quantos termos a mais vc quer ver?: '))
        contador = 0
print('Fim')
