from abc import abstractmethod
from .Node import Node


class DrawableNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def _render(self):
        pass