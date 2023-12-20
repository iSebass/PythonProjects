import sys
import pygame


#iniciamos pygame
pygame.init()

#
WIDTH  = 400 
HEIGHT = 500

#la funcion pygame regresa una superficie
surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("EL JUEGO DE iSEBAS")

#creamos el loop, donde escucharemos los eventos de la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
