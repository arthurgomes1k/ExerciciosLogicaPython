vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual ser salário? '))
anos = float(input('Em quantos anos você quer pagar? '))
parcela = vcasa / (anos * 12)

if parcela > salario - (salario * 0.70):
    print('Empréstimo negado!')
else:
    print(f'Você pagara {(anos * 12):.0f} parcelas de {parcela:.2f} R$ durante os {anos} anos!')
