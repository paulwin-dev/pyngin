from classes.nodes.core.root import Root
from classes.types.color import Color
from classes.types.dimension2 import Dimension2


class DrawableNode(Root):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._color = Color.WHITE

    
    @property
    def position(self) -> Dimension2:
        raise Exception("Unimplemented attribute, position")
    
    @position.setter
    def position(self, position: Dimension2):
        raise Exception("Unimplemented attribute, position")
    
    @property
    def size(self) -> Dimension2:
        raise Exception("Unimplemented attribute, size")
    
    @size.setter
    def size(self, size: Dimension2):
        raise Exception("Unimplemented attribute, size")
    
    @property
    def color(self) -> Color:
        return self._color