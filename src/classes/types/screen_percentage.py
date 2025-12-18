from classes.types.dimension2 import Dimension2
from classes.types.vector2 import Vector2


class ScreenPercentage(Dimension2):
    def __init__(self, x, y):
        super().__init__()
        
        self._x_percentage = x
        self._y_percentage = y

    @property
    def x(self):
        return self._x_percentage
    
    @property
    def y(self):
        return self._x_percentage
    
    def resolve(self, ctx):
        return Vector2(ctx.x * self.x, ctx.y * self.y)