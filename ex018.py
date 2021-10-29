print('=' * 15, 'Exercício 18', '=' * 15)
from math import sin, cos, tan, radians
n = int(input('Digite o ângulo para ver seu seno, cosseno e tangente:'))
seno = sin(radians(n))
cosseso = cos(radians(n))
tangente = tan(radians(n))
print('O seno de {}° é {:.2f}\nSeu cosseno é {:.2f}\nE sua tangente é {:.2f}.'.format(n, seno, cosseso, tangente))
#esse contrabarra n pula pra próxima linha sem precisar dar outro print.