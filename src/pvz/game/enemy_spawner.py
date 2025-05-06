from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import Game


class EnemySpawner:
    def __init__(self, game: "Game", enemies):
        self._game = game
        self._enemies = enemies
        self._index = 0
        self._remaining_sleep = enemies[0]["sleep"]

    def on_tick(self):
        if self._index == len(self._enemies):
            self._check_win()
            return

        if self._remaining_sleep > 0:
            self._remaining_sleep -= 1
            return

        for row in self._enemies[self._index]["rows"]:
            self._game.zombie_manager.spawn_zombie(row)

        self._index += 1
        if self._index != len(self._enemies):
            self._remaining_sleep = self._enemies[self._index]["sleep"]

    def _check_win(self):
        if self._game.zombie_manager.get_number_of_zombies() == 0:
            self._game.victory()
