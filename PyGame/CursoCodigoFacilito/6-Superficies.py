import sys
import pygame

pygame.init()

WIDTH  = 500
HEIGHT = 600

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("el Juego del Sebitas :D")


white = (255, 255, 255)
red   = (115, 38,   80)
green = ( 52, 157,  89)
blue  = ( 59,  87, 181)

surface2 = pygame.Surface( (200, 200) )
surface2.fill(green)

rect = surface2.get_rect()
rect.center = ( WIDTH//2, HEIGHT//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    surface.fill( white )

    surface.blit(surface2,rect)
    pygame.draw.rect(surface2, red,  (80,40,20,30))

    pygame.display.update()