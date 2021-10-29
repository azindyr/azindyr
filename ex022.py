from time import sleep#importa o módulo que espera
print('=' * 15, 'Exercício 22', '=' * 15)
nome = str(input('Digite seu nome completo:')).strip()#Recebe o nome da pessoa sem contar os espaços extras
separa = nome.split()#separa o nome
nome1letras = len(separa[0])#conta as letras do primeiro nome que foi separado
letras = len(nome) - nome.count(' ')#conta as letras do nome completo sem os espaços
print('Analisando seu nome...')
sleep(2)#espera 2 segundos antes de mostrar a resposta
print('Seu nome em maiúsculo fica {}.'.format(nome.upper()))#mostra o nome em maiúsculo
print('Seu nome em minúsculo fica {}.'.format(nome.lower()))#mostra o nome em minúsculo
print('Seu nome possui ao todo {} letras.'.format(letras))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], nome1letras))#coloca o primeiro nome e suas letras


