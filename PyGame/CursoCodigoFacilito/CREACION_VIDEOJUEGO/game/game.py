import sys
import pygame
import time

from .config   import *
from .platform import Platform
from .player   import Player

class Game:


    def __init__(self):
        pygame.init()
        self.WIDTH   = WIDTH
        self.HEIGHT  = HEIGHT
        self.surface = pygame.display.set_mode(  (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        self.runing  = True

    def start(self):
        self.new()

    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player   = Player(100, self.platform.rect.top-200)

        self.sprites = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)

    def run(self):
        while self.runing:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()

    def draw(self):
        self.surface.fill(BLACK)
        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()
        self.sprites.update()

        self.player.validate_platform(self.platform)

        time.sleep(0.01)

    def stop(self):
        pass