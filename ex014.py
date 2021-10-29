print('=' * 15, 'Exercício 14', '=' * 15)
print('CONVERSOR DE TEMPERATURA')
tc = float(input('Digite um atemperatura em °C:'))
tf = tc * 1.8 + 32
tk = tc + 273
print('{:.1f}°C equivalem a {:.1f}°F ou {:.1f}°K!'.format(tc, tf, tk))
