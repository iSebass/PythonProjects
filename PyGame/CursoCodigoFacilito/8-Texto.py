import sys
import pygame

pygame.init()

WIDTH = 600
HEIGH = 600

surface = pygame.display.set_mode (  (WIDTH,HEIGH) )
pygame.display.set_caption("el Jueguito de Sebas")


white = (255, 255, 255)
red   = (115, 38,   80)
green = ( 52, 157,  89)
blue  = ( 59,  87, 181)

while True:

    for event in pygame.event():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill(white)

    pygame.display.update()