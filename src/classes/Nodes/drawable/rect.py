import pygame
from classes.nodes.drawable.drawable_node import DrawableNode
from classes.types.color import Color


class Rect(DrawableNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._color: Color = Color.WHITE
        self._render_object = pygame.Rect(50, 50, 100, 100)

    def _draw(self, surface):
        pygame.draw.rect(surface, self._color, self._render_object)

    