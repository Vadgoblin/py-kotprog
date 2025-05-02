import pygame
from .game import Game
from .game import GameStatus

_clock = pygame.time.Clock()

class GameProxy:
    def __init__(self,screen, config):
        self._screen = screen
        self._game = Game(config)
        self._target_fps = config.game["target_fps"]

    def start(self):
        while self._is_game_ongoing():
            self._process_events()
            self._tick()
            self._draw()
            _clock.tick(100)

    def _is_game_ongoing(self):
        return self._game._game_status == GameStatus.ONGOING

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                self._game.on_event(event)

    def _tick(self):
        self._game.on_tick()

    def _draw(self):
        self._game.draw(self._screen)
        pygame.display.flip()