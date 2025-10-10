import enum

import pygame
from pygame import Color


class TileType(enum.Enum):
    WHITE = 0
    BLACK = 1
    BOUNDARY = 2
    EMPTY = 3


class MapTile(pygame.sprite.Sprite):
    white_tile =  pygame.image.load('./graphics/sprites/tiles/white.png')
    black_tile = pygame.image.load('./graphics/sprites/tiles/black.png')
    empty_tile = pygame.image.load('./graphics/sprites/tiles/empty.png')

    def __init__(self, XCoord, YCoord, *groups, t: TileType):
        super().__init__(*groups)
        if t == TileType.WHITE:
            self.image = self.__class__.white_tile
        elif t == TileType.BLACK:
            self.image = self.__class__.black_tile
        else:
            self.image = self.__class__.empty_tile

        self.rect = self.image.get_rect()
        self.rect.x = XCoord * self.rect.width
        self.rect.y = YCoord * self.rect.height
        self.type = t

    def __repr__(self):
        if self.type == TileType.WHITE:
            return 'W'
        if self.type == TileType.BLACK:
            return '.'
        if self.type == TileType.BOUNDARY:
            return 'R'
        if self.type == TileType.EMPTY:
            return ' '


class Map:
    def __init__(self):
        self.map_image = pygame.image.load('./graphics/test_map.png')
        self.tile_group = pygame.sprite.Group()
        self.tiles = [[None for _ in range(self.map_image.get_width())] for _ in range(self.map_image.get_height())]
        color_map = {
            (255, 255, 255, 255): TileType.WHITE,
            (0, 0, 0, 255): TileType.BLACK,
            (255, 0, 0, 255): TileType.BOUNDARY,
            (0, 0, 0, 0): TileType.EMPTY,
        }
        for y in range(self.map_image.get_height()):
            for x in range(self.map_image.get_width()):
                color = self.map_image.get_at((x, y))
                self.tiles[y][x] = MapTile(x, y, self.tile_group, t=color_map[tuple(color)])

        # for x in range(len(self.tiles)):
        #     print(self.tiles[x])
