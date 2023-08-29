frase = str(input('Digite uma frase: ')).upper()
frase = frase.replace(' ', '')
frase_inv = frase[::-1]

# com if e else:
'''print(f'A frase {frase} ao contrário é {frase_inv}')
if frase == frase_inv:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')'''

# com for:
inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
print(f'A frase {frase} ao contrário fica {inverso}')
if frase == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')