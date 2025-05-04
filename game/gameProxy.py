import pygame
from config.config import Config
from .game import Game
from .game import GameStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.level.level import Level

_clock = pygame.time.Clock()

class GameProxy:
    def __init__(self,screen):
        self._screen = screen
        self._game = None
        self._target_fps = Config().game["target_fps"]

    def start(self, level : "Level"):
        self._game = Game(level)
        while self._is_game_ongoing():
            self._process_events()
            self._tick()
            self._draw()
            _clock.tick(self._target_fps)

    def _is_game_ongoing(self):
        return self._game._game_status == GameStatus.ONGOING

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                self._game.on_event(event)

    def _tick(self):
        self._game.on_tick()

    def _draw(self):
        self._game.draw(self._screen)
        pygame.display.flip()