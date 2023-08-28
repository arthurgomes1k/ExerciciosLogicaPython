palavras = 'aprender', 'progamar', 'linguagem', 'python', 'curso'

contador = 0

for p in palavras:
    print(f'Na palavra {p.upper()} temos as vogais: ', end='')

    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()
    contador += 1
