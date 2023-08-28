
import math
g = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(g))
cos = math.cos(math.radians(g))
tan = math.tan(math.radians(g))

print(f'O seno  do ângulo {g} é {sen:.4f}')
print(f'O cosseno  do ângulo {g} é {cos:.4f}')
print(f'O tangente  do ângulo {g} é {tan:.4f}')
