import sys
import pygame

WIDTH  = 400
HEIGHT = 600

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )

pygame.display.set_caption("el juego de Isebas")

#COLOR RGB
white = (255,255,255)
red   = (127,10,15)
blue  = (0,0,255)
green = (0,255,0)

my_color = ( 200,90,130 )

backgroundColor = pygame.Color( my_color )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #actualizamos el color
    surface.fill(backgroundColor)

    #actualizamos la pantalla
    pygame.display.update()