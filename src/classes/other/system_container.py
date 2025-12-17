import time
from systems.game_loop import GameLoopManager
from systems.graphics import GraphicsManager
from systems.scripts import ScriptLoader

from ..base.engine_base import EngineBase


class SystemContainer(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._scripts: ScriptLoader
        self._graphics: GraphicsManager
        self._gameloop: GameLoopManager

        self._root = root

    def _load(self):
        self._graphics = GraphicsManager(self._root)
        self._gameloop = GameLoopManager(self._root)
        self._scripts = ScriptLoader(self._root)

        self._graphics._init()

    def _load_scripts(self):
        self._scripts._load_scripts()

    def _start_gameloop(self):
        self._gameloop._init()

    @property
    def scripts(self):
        return self._scripts
    
    @property
    def graphics(self):
        return self._graphics
    
    @property
    def game_loop(self):
        return self._gameloop