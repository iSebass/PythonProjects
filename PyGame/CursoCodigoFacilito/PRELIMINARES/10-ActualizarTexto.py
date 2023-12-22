import pygame
import sys


pygame.init()

WIDTH   = 600
HEIGHT  = 600

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("El juego de sebitas :D")

white = (255,255,255)
red   = (115,38,80)

font  = pygame.font.Font('freesansbold.ttf', 48)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    seconds = pygame.time.get_ticks() // 1000



    surface.fill(white)
    text = font.render( str(seconds), True,  red )
    rect = text.get_rect()
    rect.center = (WIDTH//2 , HEIGHT//2)

    surface.blit(text, rect)

    pygame.display.update()