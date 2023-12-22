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

'''
pygame.mixer.music.load('sounds/super-mario-bros.mp3')
pygame.mixer.music.set_volume(0.2)  #float 0.0 a 1.0
pygame.mixer.music.play()
'''
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:  #preguntamos si se presiono una tecla
           
            if e.key == pygame.K_a:    ##preguntamos si se libero una tecla
                print("Izquierda")
            if e.key == pygame.K_d:    ##preguntamos si se libero una tecla
                print("Derecha")
            if e.key == pygame.K_w:    ##preguntamos si se libero una tecla
                print("Arriba")
            if e.key == pygame.K_s:    ##preguntamos si se libero una tecla
                print("Abajo")
            

    surface.fill(white)
    pygame.display.update()