from random import randint
from time import sleep
print('=' * 15, 'Exercício 28', '=' * 15)
print('Pensarei em um número entre 0 e 5, tente adivinhar!')
pc = randint(0, 5)
jog = int(input('Digite um número: '))
print('Processando...')
sleep(2)
if jog == pc:
    print('Você ganhou! Também escolhei o número {}.'.format(jog))
else:
    print('Você errou, o número que pensei foi o {}.'.format(pc))
