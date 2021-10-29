print('=' * 15, 'Exercício 11', '=' * 15)
print('Neste programa você saberá quantos litros de tinta são necessários para pintar a sua parede!')
l = float(input('Digite a largura da parede em metros:'))
h = float(input('Digite a altura da parede em metros:'))
area = l * h
tinta = area / 2
print('Sua parede de {}X{} tem {}m².'.format(l, h, area))
print('Para pintá-la será necessário {}l de tinta.'.format(tinta))
