import sys
import pygame


pygame.init()


WIDTH   = 400
HEIGHT  = 500
surface = pygame.display.set_mode( (WIDTH , HEIGHT) )
pygame.display.set_caption("EL JUEGO DE iSebas")

white    = (255,255,255)
red      = (115,30,80)
green    = (30,180,20)
my_color = (118,30,80)

#clase para crear rectangulos
rect = pygame.Rect(100, 200, 120,60)
rect.center = ( WIDTH//2, HEIGHT//2 )

#         POSX POSY W   H
rect2 = ( 100, 100, 80, 40)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill( white )
    pygame.draw.rect(surface, red, rect)
    pygame.draw.rect(surface, green, rect2)
    pygame.display.update()