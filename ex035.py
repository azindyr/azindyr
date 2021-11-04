from time import sleep
print('=' * 15, 'Exercício 35', '=' * 15)
c1 = float(input('Digite um lado: '))
c2 = float(input('Digite outro lado: '))
c3 = float(input('Digite o terceiro lado: '))
print('Analisando...')
sleep(1.5)
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Os lados formam um triângulo.')
else:
    print('A soma dos lados não formam um triângulo')
