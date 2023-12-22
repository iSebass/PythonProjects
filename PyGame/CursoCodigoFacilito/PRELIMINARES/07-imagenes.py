import sys
import pygame

pygame.init()

WIDTH  = 600
HEIGHT = 600

surface = pygame.display.set_mode(  (WIDTH, HEIGHT)  )
pygame.display.set_caption("el Juego de Sebitas")

white = (255, 255, 255)
red   = (115, 38,   80)
green = ( 52, 157,  89)
blue  = ( 59,  87, 181)


player = pygame.image.load('img/codi.png')
rect  = player.get_rect()
rect.center = (WIDTH//2, HEIGHT//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill( white )
    surface.blit(player, rect)

    pygame.display.update()