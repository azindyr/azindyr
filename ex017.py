print('=' * 15, 'Exercício 17', '=' * 15)
from math import hypot
cat1 = float(input('Digite um cateto:'))
cat2 = float(input('Digite o segundo cateto:'))
hipo = hypot(cat1, cat2)
print('Com os catetos valendo {} e {} a hipotenusa é {:.1f}.'.format(cat1, cat2, hipo))
#Ou você pode usar o princípio matemático:
#h² = cat1²+cat2²
#hipotenusa = (cat1 ** 2 + cat2 ** 2) ** (1 / 2)
#nessa resolução acima, os catetos são primeiros elevados ao quadrado, somados e após isso é tirado a raiz quadrada dessa soma assim como é feita no papel

