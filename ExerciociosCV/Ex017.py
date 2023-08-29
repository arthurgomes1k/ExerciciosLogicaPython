
'''op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hp = (op ** 2 + ad ** 2) ** (1 / 2)

print(f'O comprimento da hipotenusa é {hp:.2f}')'''

import math
op = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hp = math.hypot(op, ad)

print(f'O comprimento da hipotenusa é {hp:.2f}')
