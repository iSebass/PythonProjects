import pygame
import sys


pygame.init()

WIDTH   = 800
HEIGHT  = 800

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("El juego de sebitas :D")

white = (255,255,255)
red   = (115,38,80)

font  = pygame.font.Font('freesansbold.ttf', 48)

'''
pygame.mixer.music.load('sounds/super-mario-bros.mp3')
pygame.mixer.music.set_volume(0.2)  #float 0.0 a 1.0
pygame.mixer.music.play()
'''

image = pygame.image.load('img/small_circle.png')
rect = image.get_rect()
rect.center = ( WIDTH//2 , HEIGHT//2 )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pos = pygame.mouse.get_pos()
    rect.center = pos

    surface.fill(white)
    surface.blit(image,rect)
    pygame.display.update()