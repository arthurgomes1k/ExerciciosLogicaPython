s = float(input('Digite o salário: '))
if s > 1250:
    print(f'Seu salário aumentou de {s} R$ para {s + (s * 0.10)} R$ com 10% de aumento.')
else:
    print(f'Seu salário aumentou de {s} R$ para {s + (s * 0.15)} R$ com 15% de aumento.')
