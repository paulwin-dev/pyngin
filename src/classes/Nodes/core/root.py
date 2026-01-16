from classes.nodes.core.world import World
from ...other.system_container import SystemContainer
from ..node import Node

class Root(Node):
    """
    Represents the root node of the hierarchical structure of the engine.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._systems: SystemContainer

        self._create_trivial_children()

    def _create_trivial_children(self):
        World(parent=self)

    def _init(self):
        self._systems = SystemContainer(self)
        self._systems._load()

    @property
    def world(self):
        return self.get_node("world")

    @property
    def engine_version(self):
        return "Alpha 5.24.3"
    
    @property
    def systems(self):
        return self._systems