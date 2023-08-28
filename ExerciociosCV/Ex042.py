l1 = float(input('Comprimento do primeiro lado: '))
l2 = float(input('Comprimento do segundo lado: '))
l3 = float(input('Comprimento do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Essas 3 retas podem formar um triângulo.')
    if l1 == l2 == l3:
        print('Essas 3 retas formão um triângulo Equilátero.')
    elif l1 == l2 != l3 or l2 == l1 != l3 or l1 == l3 != l2 or l3 == l1 != l2 or l3 == l2 != l1 or l2 == l3 != l1:
        print('Essas 3 retas fomão um triângulo Isósceles.')
    elif l1 != l2 != l3 != l1:
        print('Essas 3 retas formão um triângulo Escaleno.')
else:
    print(f'Essas 3 retas não podem formar um triângulo.')
