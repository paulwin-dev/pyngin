import pygame

from abc import abstractmethod
from classes.nodes.node import Node
from classes.types.color import Color
from classes.types.dimension2 import Dimension2


class DrawableNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._size: Dimension2
        self._position: Dimension2
        self._color: Color = Color.WHITE


    @abstractmethod
    def _draw(self, surface: pygame.Surface):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def size(self) -> Dimension2: ...

    @property.setter
    @abstractmethod
    def size(self, value: Dimension2): ...

    @property
    @abstractmethod
    def position(self, value: Dimension2) -> Dimension2: ...

    @property.setter
    @abstractmethod
    def position(self, value: Dimension2): ...

    @property
    def color(self) -> Color:
        return self._color

    @property.setter
    def color(self, value: Color):
        self._color = value