from random import choice
print('=' * 15, 'Exercício 19', '=' * 15)
al1 = str(input('Primeiro aluno:'))
al2 = str(input('Segundo aluno:'))
al3 = str(input('Terceiro aluno:'))
al4 = str(input('Quarto aluno:'))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print('O escolhido para fazer o seminário foi {}.'.format(escolhido))



