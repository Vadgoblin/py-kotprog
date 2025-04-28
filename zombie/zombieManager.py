import field
from zombie.zombie import Zombie
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from field import Field
    from plant.abstractPlant import AbstractPlant
    from bullet import Bullet


class ZombieManager:
    def __init__(self, field:"Field"):
        self._field = field
        self._zombies: List[List[Zombie]] = []
        for _ in range(field.rows):
            self._zombies.append([])

    def spawn_zombie(self, row):
        if not isinstance(row,int) or row < 0 or row >= self._field.rows:
            raise Exception(f"Expected row to be an integer between 0 and {self._field.rows - 1}, got {row}")
        self._zombies[row].append(Zombie(self, row))

    def does_plant_see_zombie(self, plant:"AbstractPlant"):
        row = plant.row
        col = plant.col
        for zombie in self._zombies[row]:
            x = field.col_to_x(col + 0.75)
            if x <= zombie.x:
                return True
        return False

    def is_zombie_blocked(self, zombie: "Zombie"):
        return self.get_blocking_plant(zombie) is not None

    def get_blocking_plant(self, zombie: "Zombie"):
        return self._field.plant_manager.get_blocking_plant(zombie)

    def get_zombie_hit_by_bullet(self, bullet: "Bullet"):
        row = bullet.row
        for zombie in self._zombies[row]:
            if zombie.is_hit_by_bullet(bullet):
                return zombie
        return None

    def draw(self, screen):
        for row in range(self._field.rows):
            for zombie in self._zombies[row]:
                zombie.draw(screen)

    def on_tick(self):
        for row in range(self._field.rows):
            for zombie in self._zombies[row]:
                if not zombie.is_alive:
                    self._zombies[zombie.row].remove(zombie)
                else:
                    zombie.on_tick()
