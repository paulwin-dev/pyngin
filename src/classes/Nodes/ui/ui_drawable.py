from classes.nodes.core.drawable_node import DrawableNode
from classes.types.screen_percentage import ScreenPercentage
from core.types import UIDimension2


class UIDrawable(DrawableNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._position: UIDimension2 = ScreenPercentage(0, 0)
        self._size: UIDimension2 = ScreenPercentage(.1, .1)

    @property
    def position(self) -> UIDimension2:
        return self._position
    
    @property.setter
    def position(self, value: UIDimension2):
        self._position = value

    @property
    def size(self) -> UIDimension2:
        return self._position
    
    @property.setter
    def size(self, value: UIDimension2):
        self._size = value