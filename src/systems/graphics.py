import pygame

from classes.base.engine_base import EngineBase
from classes.graphics.window import Window
from core import logger


class GraphicsManager(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root
        self._renderer = Renderer(root)

    def _init(self):
        self._window = Window(self._root)

    def _render_frame(self):
        self._renderer.render_world()
        pygame.display.flip()

    @property
    def window(self):
        return self._window
    
class Renderer(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root

    def render_world(self):
        for node in self._root.world.get_children():
            logger.info(node)