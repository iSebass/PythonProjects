import pygame
import sys


pygame.init()

WIDTH   = 800
HEIGHT  = 800

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

image = pygame.image.load('img/small_circle.png')
rect = image.get_rect()
rect.center = ( WIDTH//2 , HEIGHT//2 )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        rect.y -= 5
    if pressed[pygame.K_s]:
        rect.y += 5
    if pressed[pygame.K_a]:
        rect.x -= 5
    if pressed[pygame.K_d]:
        rect.x += 5

    if rect.left < 0:
        rect.left = 0
    if rect.right > WIDTH:
        rect.right = WIDTH
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT

    surface.fill(white)
    surface.blit(image,rect)
    pygame.display.update()