import os
import sys
import pygame
import time
import random

from .config   import *
from .platform import Platform
from .player   import Player
from .wall     import Wall
from .coin     import Coin


class Game:


    def __init__(self):
        pygame.init()
        self.WIDTH   = WIDTH
        self.HEIGHT  = HEIGHT
        self.surface = pygame.display.set_mode(  (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        self.runing  = True
       

        self.dir        = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'sources/Sounds')

        self.font = pygame.font.match_font(FONT)

        self.clock = pygame.time.Clock()

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.playing = True
        self.score = 0
        self.lvl = 0
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player   = Player(100, self.platform.rect.top-200)
        

        self.sprites = pygame.sprite.Group()
        self.walls   = pygame.sprite.Group()
        self.Coins   = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_walls()
        

        

    def generate_coin(self):
        last_position = WIDTH+100

        if not len(self.Coins)>0:
            for c in range(0,MAX_COINS):
                pos_x = random.randrange(last_position+180, last_position+300)
                coin = Coin(pos_x,150)
                last_position = coin.rect.right

                self.sprites.add(coin)
                self.Coins.add(coin)
        
    def generate_walls(self):

        last_position = WIDTH+100

        if not len(self.walls)>0:
            for w in range(0,MAX_WALLS):
                left = random.randrange(last_position+200, last_position+400)
                wall = Wall(left, self.platform.rect.top)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

            self.lvl +=1
            self.generate_coin()

    def run(self):
        while self.runing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()
        
        if key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        self.surface.fill(BLACK)
        self.draw_text()
    
        self.sprites.draw(self.surface)
        pygame.display.flip()

    def draw_text(self):
        self.display_text( "Score: "+str(self.score), 36, WHITE, WIDTH//2, TEXT_POS_Y)
        self.display_text( "Nivel: "+str(self.lvl), 36, WHITE, WIDTH//10, TEXT_POS_Y)
        if not self.playing:
             self.display_text( "Perdiste !!", 60, WHITE, WIDTH//2, HEIGHT//2)
             self.display_text( "Press R to Reload", 35, WHITE, WIDTH//2, 100)

    def display_text(self, text, size, color, posx, posy):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (posx, posy)

        self.surface.blit(text, rect)

    def update(self):
        if self.playing:
            wall = self.player.collide_with(self.walls)
            if wall:
                if self.player.collide_bottom(wall):
                    self.player.skid(wall)
                else:
                    self.stop()

            coin = self.player.collide_with(self.Coins)
            if coin:
                self.score += 1
                
                coin.kill()
                sound = pygame.mixer.Sound( os.path.join(self.dir_sounds, 'Coin02.mp3') )   
                sound.play()
                print(self.score)

            self.sprites.update()
            self.player.validate_platform(self.platform)

            self.update_elements(self.walls)
            self.update_elements(self.Coins)
            self.generate_walls()

    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right>0:
                element.kill()

    def stop(self):
        self.player.stop()
        sound = pygame.mixer.Sound( os.path.join(self.dir_sounds, 'Losser.mp3') )   
        sound.play()
        self.stop_elements(self.walls)
        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()

    def menu(self):
        self.surface.fill(GREEN_LIGHT)
        self.display_text('Presiona Una tecla para comenzar',36, BLACK, WIDTH//2, 10)
        pygame.display.flip()
        self.wait()

    def wait(self):
        wait = True
        while wait:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.runing = False
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    wait = False

    