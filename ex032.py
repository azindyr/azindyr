import datetime
print('=' * 15, 'Exercício 32', '=' * 15)
print('Este programa analisará se o ano digitado é BISSEXTO ou não.')
ano = int(input('Que ano quer analisar? Coloque 0 para ver o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))
#Lembrando que para o ano ser bissexto ele deve ser:
#Divisível por 4, ou seja, o resto da divisão por 4 deve ser 0 e;
#Não divisível por 100, ou seja, o resto da divisão por 100 deve ser diferente de 0 ou;
#Divisível por 400, ou seja, o resto da divisão por 400 deve ser 0.