print('=' * 15, 'Exercício 15', '=' * 15)
print('Aluguel de Carros')
print('Obs: São R$60 por dia + R$0.15 por kilômetro rodado.')
dia = int(input('Quantos dia(s) você ficou com o carro?'))
km = float(input('Quantos kilômetros foram rodados?'))
conta = dia * 60 + km * 0.15
print('Sua conta tem o total de R${:.2f}'.format(conta))
