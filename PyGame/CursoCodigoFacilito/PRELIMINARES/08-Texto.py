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

#1-  Se obtiene una fuente de texto
font_txt = pygame.font.Font('freesansbold.ttf',48)

#2. Cremamos el texto
surface_font = font_txt.render('Hola mundo', True, red )


#3- Obtenemos rectangulo

rect = surface_font.get_rect()
rect.center = (WIDTH//2, HEIGH//2)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill(white)
    surface.blit(surface_font, rect)

    pygame.display.update()