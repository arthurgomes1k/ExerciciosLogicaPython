n = int(input('Digite o número de elementos da sequência fibonacci que você quer ver: '))
contador = 0
termoanterior = 0
proximotermo = 1

print(termoanterior, '>', end=' ')
print(proximotermo, '>', end=' ')

while contador < (n - 2):
    proximotermo += termoanterior
    termoanterior = proximotermo - termoanterior
    print(proximotermo, '>', end=' ')
    contador += 1
print('Fim')
