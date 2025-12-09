from queue import Queue
import sys
import pygame

from classes.base.engine_base import EngineBase


class GameLoopManager(EngineBase):
    def __init__(self, root) -> None:
        super().__init__()

        self._root = root

        self.fps = 60
        self.clock = pygame.time.Clock()

        self._action_queue = Queue()

    def _init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            while not self._action_queue.empty():
                func, args, kwargs = self._action_queue.get()
                func(*args, **kwargs)

            pygame.display.flip()
            self.clock.tick(self.fps)
