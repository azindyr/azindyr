print('=' * 15, 'Exercício 25', '=' * 15)
nome = str(input('Digite o seu nome completo: ')).strip().upper()
analise = 'SILVA' in nome
print('Seu nome tem Silva? {}.'.format(analise))
