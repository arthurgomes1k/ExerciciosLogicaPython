n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2

if md < 5:
    print('Aluno Reprovado!')
elif 5 <= md < 7:
    print('Aluno em Recuperação!')
elif md >= 7:
    print('Aluno Aprovado!')
