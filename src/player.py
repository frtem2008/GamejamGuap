import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.coords = []
        self.image = pygame.image.load('./graphics/sprites/player/player.png')
        self.rect = self.image.get_rect()

