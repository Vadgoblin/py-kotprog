import field
import spriteLoader
from config import Config
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zombie.zombieManager import ZombieManager
    from plant.abstractPlant import AbstractPlant

config = Config().zombie
offset_x = config["offset_x"]
offset_y = config["offset_y"]
spawn_x = config["spawn_x"]

def _load_sprite():
    size = (config["width"], config["height"])
    sprite_path = config["sprite"]
    return spriteLoader.load(sprite_path,size)


class Zombie:
    def __init__(self,zombie_manager : "ZombieManager", row):
        self._zombie_manager = zombie_manager
        self._row = row
        self._y = field.row_to_y(row)
        self._x = spawn_x
        self._width = config["width"]
        self._hp = config["hp"]
        self._eat_timeout = 0
        self._sprite = _load_sprite()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def row(self):
        return self._row

    @property
    def width(self):
        return self._width

    @property
    def is_alive(self):
        return self._hp > 0

    def is_hit_by_bullet(self, bullet:"Bullet"):
        return self._x <= bullet.x + bullet.width and self._x + self._width >= bullet.x

    def suffer_damage(self):
        self._hp -= 1

    def draw(self, screen):
        position = (self._x + offset_x, self._y + offset_y)
        screen.blit(self._sprite, position)

    def on_tick(self):
        blocking_plant = self._zombie_manager.get_blocking_plant(self)
        if blocking_plant is not None:
            self._eat(blocking_plant)
        else:
            self._move()

    def _move(self):
        self._x -= 1

    def _eat(self, plant: "AbstractPlant"):
        if self._eat_timeout > 0:
            self._eat_timeout -= 1
        else:
            plant.suffer_damage()
            self._eat_timeout = config["eat_timeout"]