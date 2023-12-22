import pygame
import sys


pygame.init()

WIDTH   = 800
HEIGHT  = 800

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("El juego de sebitas :D")

white = (255,255,255)
red   = (115,38,80)
green    = (30,180,20)

font  = pygame.font.Font('freesansbold.ttf', 48)

'''
pygame.mixer.music.load('sounds/coin.mp3')
pygame.mixer.music.set_volume(0.2)  #float 0.0 a 1.0
pygame.mixer.music.play()
'''

img1 = pygame.image.load('img/small_circle.png')
rect1 = img1.get_rect()
rect1.center = (WIDTH//2 , HEIGHT//2 )

surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill( (0,0,0, 50) )
rect2 = surface2.get_rect()
rect2.center = rect1.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    
    surface.fill(white)

    surface.blit(img1, rect1)
    surface.blit(surface2, rect2)
    
    pygame.display.update()