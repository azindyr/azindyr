print('=' * 15, 'Exercício 34', '=' * 15)
s = float(input('Digite o salário do funcionário R$:'))
aumento = s + (s * 10 / 100)
if s <= 1200:
    aumento = s + (s * 15 / 100)
    print('Com o aumento de 15% o salário agora vale R${:.2f}'.format(aumento))
else:
    print('Com o aumento de 10% o salário vale R${:.2f}'.format(aumento))
