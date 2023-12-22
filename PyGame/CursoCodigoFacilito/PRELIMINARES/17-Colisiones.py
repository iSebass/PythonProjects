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

rect1 = pygame.Rect(0,0,100,80)
rect1.center = ( WIDTH//2 , HEIGHT//2 )

rect2 = pygame.Rect(0,0,100,80)

font = pygame.font.Font('freesansbold.ttf', 48)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    
    surface.fill(white)

    pos = pygame.mouse.get_pos()
    rect2.center = pos
    
    pygame.draw.rect(surface, green, rect1)
    pygame.draw.rect(surface, red, rect2)

    

    if rect1.colliderect(rect2):
        text = font.render( ":C", True,  red )
        sound = pygame.mixer.Sound('sounds/coin.mp3')
        sound.set_volume(0.2)
        sound.play()
        
    else: 
        text = font.render( ":3", True,  green )
    rect3 = text.get_rect()
    rect3.midtop = (WIDTH//2, 50)
    surface.blit(text, rect3)
    pygame.display.update()