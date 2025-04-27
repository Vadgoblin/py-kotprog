from zombie import Zombie
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from field import Field

class ZombieManager:
    def __init__(self, field:"Field"):
        self._field = field
        self._zombies = []
        for _ in range(field.rows):
            self._zombies.append([])

    def spawn_zombie(self, row):
        if not isinstance(row,int) or row < 0 or row >= self._field.rows:
            raise Exception(f"Expected row to be an integer between 0 and {self._field.rows - 1}, got {row}")
        self._zombies[row].append(Zombie(row))

    def draw(self, screen):
        self._iterate_zombies(Zombie.draw, screen)

    def on_tick(self):
        self._iterate_zombies(Zombie.on_tick)

    def _iterate_zombies(self, action, *args):
        for row in range(self._field.rows):
            for zombie in self._zombies[row]:
                action(zombie, *args)