import pygame
import sys
import math


pygame.init()

WIDTH   = 900
HEIGHT  = 900

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

img1 = pygame.image.load('img/small_circle.png')

#Escalizamos la imagen para que sea mas pequena
scale_factor = 0.6
original_size = img1.get_size()
new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))

# Escala la imagen
img1 = pygame.transform.scale(img1, new_size)


#Creamos los objetos a dibujar
rect1 = img1.get_rect()
rect1.center = (WIDTH // 2, HEIGHT // 2)

surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill( (0,0,0, 50) )

rect2 = surface2.get_rect()
rect2.center = rect1.center


rect3 = img1.get_rect()
rect3.center = (WIDTH//2-200 , HEIGHT//2-200 )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #calculamos la distancia entre los radios
    x_1 = rect1.x
    y_1 = rect1.y
    x_3 = rect3.x
    y_3 = rect3.y
    x = x_3-x_1
    y = y_3-y_1
    dist = math.hypot(x,y)


    if dist < 256 :
        text = font.render( "Colision!", True,  red )
        sound = pygame.mixer.Sound('sounds/coin.mp3')
        sound.set_volume(0.2)
        sound.play()
        
    else: 
        text = font.render( " ", True,  green )
    
    rectTxt = text.get_rect()


    #Movimiento del RECT3
    pos = pygame.mouse.get_pos()
    rect3.center = pos
    
    surface.fill(white)

    surface.blit(img1, rect1)
    surface.blit(surface2, rect2)
    surface.blit(img1, rect3)
    surface.blit(text, rectTxt)
   
    pygame.display.update()