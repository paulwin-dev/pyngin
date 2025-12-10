import pygame

from abc import abstractmethod
from classes.nodes.node import Node


class DrawableNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._sprite: pygame.Sprite
        self._surface: pygame.Surface