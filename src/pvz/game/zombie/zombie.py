from typing import TYPE_CHECKING

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game import sound_player, field
from src.pvz.game.bullet.bullet import Bullet

if TYPE_CHECKING:
    from src.pvz.game.zombie.zombie_manager import ZombieManager
    from src.pvz.game.plant.plants.abstract_plant import AbstractPlant


class Zombie:
    def __init__(self, zombie_manager: "ZombieManager", row):
        config = Config().zombie
        self._zombie_manager = zombie_manager
        self._row = row
        self._y = field.row_to_y(row)
        self._x = config["spawn_x"]
        self._offset_x = config["offset_x"]
        self._offset_y = config["offset_y"]
        self._width = config["width"]
        self._height = config["height"]
        self._hp = config["hp"]
        self._eat_timeout = 0

        size = (self._width, self._height)
        sprite_path = config["sprite"]
        self._sprite = load_sprite(sprite_path, size)

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

    def is_hit_by_bullet(self, bullet: "Bullet"):
        return self._x <= bullet.x + bullet.width and self._x + self._width >= bullet.x

    def suffer_damage(self, amount=1):
        self._hp -= amount

    def draw(self, screen):
        position = (self._x + self._offset_x, self._y + self._offset_y)
        screen.blit(self._sprite, position)

    def on_tick(self):
        blocking_plant = self._zombie_manager.get_blocking_plant(self)
        if blocking_plant is not None:
            self._eat(blocking_plant)
        else:
            self._move()

    def _move(self):
        self._x -= 1 / 3

    def _eat(self, plant: "AbstractPlant"):
        if self._eat_timeout > 0:
            self._eat_timeout -= 1
        else:
            plant.suffer_damage()
            sound_player.play_chomp()
            self._eat_timeout = Config().zombie["eat_timeout"]
