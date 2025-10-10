import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.coords = [128, 128]
        self.image = pygame.image.load('./graphics/sprites/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.coords[0] * self.rect.width
        self.rect.y = self.coords[1] * self.rect.height

