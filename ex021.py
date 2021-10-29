import pygame
print('=' * 15, 'Exercício 21', '=' * 15)
print('"Ah como todas as mulheres!"-Mestre Esqueleto')
pygame.init() #inicia o pygame
pygame.mixer.init() #inicia o tocador de sons do pygame
pygame.mixer.music.load('esqueleto.mp3') #importa o som para o pygame
pygame.mixer.music.play() #toca o som
input()
pygame.event.wait() #espera o som terminar











