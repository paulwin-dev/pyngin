import pygame

from abc import abstractmethod
from classes.nodes.node import Node


class DrawableNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._surface: pygame.Surface

    @abstractmethod
    def _draw(self, surface):
        raise NotImplementedError
        