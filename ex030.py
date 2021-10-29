from time import sleep
print('=' * 15, 'Exercício 30', '=' * 15)
print('Analisador de números.')
n = int(input('Digite um número para saber se ele é PAR ou ÍMPAR: '))
print('Analisando resultado...')
sleep(1)
if n % 2 == 0 and n != 0:
    print('O número {} é PAR.'.format(n))
elif n == 0:
    print('O número {} é Neutro.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))
