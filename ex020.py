from random import shuffle
print('=' * 15, 'Exercício 20', '=' * 15)
al1 = str(input('Primeiro aluno:'))
al2 = str(input('Segundo aluno:'))
al3 = str(input('Terceiro aluno:'))
al4 = str(input('Quarto aluno:'))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
