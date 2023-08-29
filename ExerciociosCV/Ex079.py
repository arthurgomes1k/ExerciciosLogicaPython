numero_de_alunos = int(input('Informe a quantidade de alunos: '))

erros = 0
pior_teste = 0
lista_dos_piores = []

for aluno in range(1, numero_de_alunos+1):
    teste = input('Digite a saída dos testes: ')
    for indice in teste:
        if indice == 'f':
            erros += 1

    if erros > pior_teste:
        pior_teste = erros
        pior_aluno = aluno
        lista_dos_piores = []
        lista_dos_piores.append(pior_aluno)
    elif erros == pior_teste:
        pior_aluno = aluno
        lista_dos_piores.append(pior_aluno)

    erros = 0

if len(lista_dos_piores) > 1:
    print(f'Os alunos {lista_dos_piores} erraram {pior_teste} teste(s)')
else:
    print(f'O aluno {lista_dos_piores} errou {pior_teste} teste(s)')
