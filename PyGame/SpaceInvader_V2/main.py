import pygame
import os
import time 
import random

#Creamos el lienzo donde vamos a trabajar
pygame.font.init()
WIDTH, HEIGHT = 700,700
window = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('INVADERS SPACE')

#Cargamos las imagenes de enemigos
RED_SPACE   = pygame.image.load('assets/pixel_ship_red_small.png' )
GREEN_SPACE = pygame.image.load('assets/pixel_ship_green_small.png')
BLUE_SPACE  = pygame.image.load('assets/pixel_ship_blue_small.png')

#cargamos imagen del jugador
YELLOW_SPACE = pygame.image.load('assets/pixel_ship_yellow.png')

#cargamos laser
RED_LASER     = pygame.image.load('assets/pixel_laser_red.png')
GREEN_LASER   = pygame.image.load('assets/pixel_laser_green.png')
BLUE_LASER    = pygame.image.load('assets/pixel_laser_blue.png')
YELLOW_LASER  = pygame.image.load('assets/pixel_laser_yellow.png')

# Cargamos el fondo de la ventana
BG = pygame.transform.scale( pygame.image.load('assets/background-black.png'), (WIDTH,HEIGHT) )

#creamos colores a utilizar
WHITE_COLOR = (255,255,255)

#Atributos del jugador
player_vel = 5

class Ship():
    def __init__(self,x,y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.laser_img = None
        self.ship_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y) )

    def get_width(self):
        return self.ship_img.get_width()

    def get_heigh(self):
        return self.ship_img.get_width()

class Player(Ship):
    def __init__(self, x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img   = YELLOW_SPACE
        self.laser_img  = YELLOW_LASER
        self.mask       = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP= {
          "red":(RED_SPACE, RED_LASER),
        "green":(GREEN_SPACE, RED_LASER),
         "blue":(BLUE_SPACE, RED_LASER)
    }
    def __init__(self, x,y, color, health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self,vel):
        #self.x += vel
        self.y += vel
        


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5

    enemies = []
    wave_length = 5
    enemy_vel = 1

    clock = pygame.time.Clock()

    main_font = pygame.font.SysFont("comicsans", 30)
    
    player = Player(WIDTH//2, HEIGHT//2+100)

    
    
    def redraw_window():
        window.blit(BG, (0,0) )
        #daw text
        lives_label  = main_font.render(f"Lives: {lives}", 1, WHITE_COLOR)
        level_label = main_font.render(f"Level: {level}", 1, WHITE_COLOR)
        window.blit(lives_label, (10,10))
        window.blit(level_label, (WIDTH- level_label.get_width()-10, 10))

        player.draw(window)

        for enemy in enemies:
            enemy.draw(window)

        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        
        if len(enemies) == 0:
            level += 1
            wave_length = 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(80, WIDTH-100), 
                              random.randrange(-100,-50),
                              random.choice(["red","green","blue"]))
                enemies.append( enemy )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]  and player.x - player_vel > 0:
            player.x -= player_vel
        if key[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if key[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if key[pygame.K_DOWN] and player.y + player_vel + player.get_heigh() < HEIGHT:
            player.y += player_vel
        
        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_heigh() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        redraw_window()
main()

