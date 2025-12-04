import pygame

import config

_window: pygame.Surface

def _init():
    global _window
    _window = pygame.display.set_mode((config.DEFAULT_WIDTH, config.DEFAULT_HEIGHT), pygame.RESIZABLE)
    
def set_fullscreen(fullscreen: bool):
    global _window
    _window = pygame.display.set_mode(flags=pygame.FULLSCREEN)