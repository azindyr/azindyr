print('=' * 15, 'Exercício 12', '=' * 15)
print('O GERENTE FICOU MALUCO! SÃO 10% DE DESCONTO NA LOJA TODA!')
p = float(input('Digite o preço do produto R$'))
desconto = p - (p * 10 / 100)
print('O produto custava R${:.2f}, agora com o desconto de 10% custa R${:.2f}'.format(p, desconto))
