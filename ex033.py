print('=' * 15, 'Exercício 33', '=' * 15)
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
maior = n1
menor = n2
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n2 and n3 < n1:
    menor = n3
print('O maior é {}.'.format(maior))
print('O menor é {}.'.format(menor))
