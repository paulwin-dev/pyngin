import sys
import pygame

from gameloop import renderer

import config

_clock = pygame.time.Clock()

def init():
    pygame.init()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        renderer.render()
        _clock.tick(config.DEFAULT_FPS)