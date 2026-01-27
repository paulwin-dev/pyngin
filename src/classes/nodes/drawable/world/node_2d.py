from classes.nodes.node import Node


class Node2D(Node):
    """
    A node related to the engine's world rendering
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def can_render(self):
        return not isinstance(self, Node2D)