from queue import Queue
import sys
import pygame

from classes.base.engine_base import EngineBase
from core import logger


class GameLoopManager(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root

        self.fps = 60
        self.clock = pygame.time.Clock()

        self._action_queue = Queue()
        self._error_queue = Queue()

    def _init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            while not self._action_queue.empty():
                func, args, kwargs = self._action_queue.get()
                func(*args, **kwargs)

            while not self._error_queue.empty():
                error = self._error_queue.get()
                logger.error(error)

            pygame.display.flip()
            self.clock.tick(self.fps)
