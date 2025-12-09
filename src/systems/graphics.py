from classes.base.engine_base import EngineBase
from classes.graphics.window import Window


class GraphicsManager(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root

    def _init(self):
        self._window = Window(self._root)

    @property
    def window(self):
        return self._window