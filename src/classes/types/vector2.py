import math

from classes.types.dimension2 import Dimension2


class Vector2(Dimension2):
    ZERO: "Vector2"

    def __init__(self, x: float = 0, y: float = 0) -> None:
        super().__init__()
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    @property
    def normalized(self):
        mag = self.magnitude
        return Vector2(self.x / mag, self.y / mag)
    
    def resolve(self, ctx):
        return self
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, other: "Vector2 | float | int"):
        if type(other) == int or type(other) == float:
            return Vector2(self.x + other, self.y + other)
        
        if type(other) != Vector2:
            raise Exception(f"Unable to perform arithmetic on Vector2 and {type(other).__name__}.")
        
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Vector2 | float | int"):
        if type(other) == int or type(other) == float:
            return Vector2(self.x - other, self.y - other)
        
        if type(other) != Vector2:
            raise Exception(f"Unable to perform arithmetic on Vector2 and {type(other).__name__}.")
        
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x * other, self.y * other)
        
        if type(other) != Vector2:
            raise Exception(f"Unable to perform arithmetic on Vector2 and {type(other).__name__}.")
        
        return Vector2(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x / other, self.y / other)
        
        if type(other) != Vector2:
            raise Exception(f"Unable to perform arithmetic on Vector2 and {type(other).__name__}.")
        
        return Vector2(self.x / other.x, self.y / other.y)
    
Vector2.ZERO = Vector2()