import pygame
from config.config import Config
from .game import Game
from .game import GameStatus
from typing import TYPE_CHECKING
from .gameoverScreen import display_victory_screen, display_defeat_screen

if TYPE_CHECKING:
    from game.level.level import Level
    from pygame.surface import Surface

_clock = pygame.time.Clock()

class GameProxy:
    def __init__(self,screen : "Surface"):
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

        if self._game.game_status == GameStatus.DEFEAT:
            display_defeat_screen(self._screen)
        elif self._game.game_status == GameStatus.VICTORY:
            display_victory_screen(self._screen)

    def _is_game_ongoing(self):
        return self._game.game_status == GameStatus.ONGOING

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