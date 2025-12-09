from ..base.engine_base import EngineBase

class Color(EngineBase):
    def __init__(self, r, g, b) -> None:
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r
    
    @property
    def g(self):
        return self._g
    
    @property
    def b(self):
        return self._b
    
    def __str__(self) -> str:
        return f"({self.r}, {self.g}, {self.b})"