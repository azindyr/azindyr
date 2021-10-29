print('=' * 15, 'Exercício 10', '=' * 15)
print('Conversor de moedas(12/10/2021)')
m = float(input('Digite a quantidade que desejas converter R$'))
dolar = m / 5.54
euro = m / 6.40
libra = m / 7.55
iene = m * 20.49
print('Com R${:.2f} você pode comprar US${:.2f}. \n€{:.2f}.\n£{:.2f}.\n¥{:.2f}'.format(m, dolar, euro, libra, iene))

