# faça um programa que leia uma frase e mostre:
# a) quantas vezes aparece a letra "A".
# b) em que posição ela aparece a primeira vez.
# c) em que posição aparece a ultima vez.

frase = str(input('Digite uma frase: ')).strip()
fa = frase.upper().count('A')
pa = frase.upper().find('A')+1
ua = frase.upper().rfind('A')+1

print(f'A frase tem {fa} letra(s) A.')
print(f'O primeiro a está na posição {pa}.')
print(f'O ultimo a está na posição {ua}')
