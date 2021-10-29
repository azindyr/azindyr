print('=' * 15, 'Exercício 13', '=' * 15)
sal = float(input('Digite o salário do funcionário R$'))
quinze = sal * 15 / 100
novo = sal + (sal * 15 / 100)
print('Com o reajuste de 15% adicional(que é R${:.2f}), o salário será R${:.2f}'.format(quinze, novo))


