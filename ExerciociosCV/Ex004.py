
n = input('Digite algo:')
t = type(n)
num = n.isnumeric()
alfa = n.isalpha()
alnu = n.isalnum()
esp = n.isspace()
mai = n.isupper()
min = n.islower()
cap = n.istitle()

print(f'O tipo primitivo de de {n} é {t}')
print(f'{n} é numerico? {num}')
print(f'{n} é alfabetico? {alfa}')
print(f'{n} é alfanumerico? {alnu}')
print(f'{n} so tem espaços? {esp}')
print(f'{n} está em maiúsculas? {mai}')
print(f'{n} está em minúsculas? {min}')
print(f'{n} é capitalizada? {cap}')