import pygame
from sys import exit
import math

# Game init --------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------- #
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("a")

# Establishing game time -------------------------------------------------------------------------------- #
clock = pygame.time.Clock()
tick = 0

# Ingame fonts -- got 'em from Google Fonts https://fonts.google.com/specimen/Tektur -------------------- #
font_default = pygame.font.Font('fonts/Tektur-Regular.ttf', 50)

# Sample background texture ----------------------------------------------------------------------------- #
surface_background = pygame.image.load('graphics/background/clouds.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(surface_background, (0,0))
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
exit()
