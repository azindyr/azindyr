from time import sleep
print('=' * 15, 'Exercício 31', '=' * 15)
print('A passagem será calculada da seguinte forma: até 200km será cobrado R$0,50 por km, '
      'acima disso o preço por km é R$0,45')
km = float(input('Digite a distância(em km) da viagem: '))
passagem = km * 0.50
print('Calculando preço...')
sleep(1.5)
if km > 200:
    passagem = km * 0.45
    print('Como a viagem é maior do que 200 km, o valor da passagem fica R${:.2f}.'.format(passagem))
else:
    print('O valor da passagem é R${:.2f}.'.format(passagem))
