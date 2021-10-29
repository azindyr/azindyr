print('=' * 15, 'Exercício 23', '=' * 15)
n = int(input('Digite um número de 0 a 9999:'))
print('Unidade {}.'.format(n // 1 % 10))
print('Dezena {}.'.format(n // 10 % 10))
print('Centena {}.'.format(n // 100 % 10))
print('Unidade de milhar {}.'.format(n // 1000 % 10))



