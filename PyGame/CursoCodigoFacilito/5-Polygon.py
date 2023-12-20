import sys
import pygame


pygame.init()

WIDTH  = 400
HEIGHT = 600

surface  = pygame.display.set_mode(  (WIDTH, HEIGHT)  )
pygame.display.set_caption("el Jueguito de Sebas :D")


white = (255, 255, 255)
red   = (115, 38,   80)
green = ( 52, 157,  89)
blue  = ( 59,  87, 181)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        surface.fill( white )
        
        #draw
        '''
        pygame.draw.rect(surface, red, (100,100,80,40) )
        pygame.draw.circle(surface, green, (50,50),50)
        pygame.draw.line(surface, red, (100,100),(30,40),10 )
        '''

        pygame.draw.polygon(surface, green, ( 
                (0,400), 
                (100,300), 
                (200,400) 
            )
        )

        pygame.display.update()