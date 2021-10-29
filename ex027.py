print('=' * 15, 'Exercício 27', '=' * 15)
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('É um prazer te conhecer!')
print('Seu primeiro nome é {},\n e seu ultimo é {}.'.format(separa[0], separa[-1]))

