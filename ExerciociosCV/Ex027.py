# Faça um programa que leia o nome completo de uma pessoa mostrando...
# ...o primeiro e o ultimo nome separados.

nome = str(input('Digite seu nome completo: ')).strip()
ns = nome.split()

print(f'Primeiro nome: {ns[0]}')
print(f'Ultimo nome: {ns[-1]}')
