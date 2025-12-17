import pygame

from classes.base.engine_base import EngineBase
import constants


class Window(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root
        self._surface = pygame.display.set_mode((constants.DEFAULT_WIDTH, constants.DEFAULT_HEIGHT), pygame.RESIZABLE)

        self._fullscreen = False

        pygame.display.set_caption("pyngin")

    @property
    def fullscreen(self):
        return self._fullscreen
    
    @fullscreen.setter
    def fullscreen(self, value: bool):

        
        self._fullscreen = value
        self._root.systems.game_loop._action_queue.put((self._mt_update_fullscreen, (), {}))
        

    def _mt_update_fullscreen(self):
        if self.fullscreen:
            self._surface = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
        else:
            self._surface = pygame.display.set_mode((constants.DEFAULT_WIDTH, constants.DEFAULT_HEIGHT), pygame.RESIZABLE)