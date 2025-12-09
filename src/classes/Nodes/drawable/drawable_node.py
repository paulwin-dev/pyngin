from abc import abstractmethod
from classes.nodes.node import Node


class DrawableNode(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    @abstractmethod
    def render(self):
        pass