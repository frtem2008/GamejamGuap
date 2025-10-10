import pygame
from pygame.locals import *

from map import Map
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Guap gamejam autumn")
        self.running = True
        self.players = pygame.sprite.Group()
        self.player = Player(self.players)
        self.map = Map()
        self.backdround_image = pygame.image.load('graphics/background/clouds.png')

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    ...
                if event.type == KEYUP:
                    ...

            self.map.tile_group.update(self.screen)
            self.players.update()
            # self.screen.fill((168, 168, 96))
            self.screen.blit(self.backdround_image, (0, 0))
            self.map.tile_group.draw(self.screen)
            self.players.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
