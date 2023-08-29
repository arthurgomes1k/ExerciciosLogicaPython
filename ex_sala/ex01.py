# Enunciado: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem considerar espaços.
# Quantas letras tem o primeiro nome?

nome = str(input('Digite seu nome completo: '))
sem_esp = nome.replace(" ", "")
letras_nome = nome.split()

print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo', len(sem_esp))
print('Seu primeiro nome tem', len(letras_nome[0]))
