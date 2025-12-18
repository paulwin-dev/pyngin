from abc import abstractmethod
from classes.base.engine_base import EngineBase
from classes.types.vector2 import Vector2


class Dimension2(EngineBase):
    """
    An abstract parent class for all data types related to representing a dimension in 2D space.
    """

    @abstractmethod
    def resolve(self, ctx: Vector2) -> Vector2:
        """
        Resolves this dimension into an absolute pixel-space Vector2
        using the provided layout context.

        
        **Params:** \n
        `ctx`: A Vector2 that represent's the parent's dimension
        """

        raise NotImplementedError