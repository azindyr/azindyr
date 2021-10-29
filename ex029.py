from time import sleep
print('=' * 15, 'Exercício 29', '=' * 15)
v = int(input('Qual a velocidade do carro: '))
if v <= 80:
    print('Você está dentro do limite da pista, continue assim!')
else:
    multa = (v - 80) * 7
    print('Calculando multa...')
    sleep(2)
    print('Você estava em alta velocidade {}km/h acima do limite que é 60, por isso pa'
          'gará uma multa de R${:.2f}'.format(v - 80, multa))
