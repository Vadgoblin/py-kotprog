from config.config import Config
from game import spriteLoader
from game.plant.plants.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.plant.plantManager import PlantManager


config = Config().plant


def _get_sprite():
    sprite_path = config["cherrybomb"]["sprite"]
    width = config["width"]
    height = config["height"]
    return spriteLoader.load(sprite_path, (width, height))

class Cherrybomb(AbstractPlant):
    def __init__(self, plant_manager: "PlantManager", row, col):
        hp = config["cherrybomb"]["hp"]
        super().__init__(plant_manager, row, col, hp)
        self._sprite = _get_sprite()
        self._explode_time = config["cherrybomb"]["explode_time"]
        self._damage = config["cherrybomb"]["damage"]

    def on_tick(self):
        if self._explode_time > 0:
            self._explode_time -= 1
            return
        else:
            self._explode()

    def _explode(self):
        zombies = self._plant_manager._game.zombie_manager.get_nearby_zombies(self._row, self._col)
        for zombie in zombies:
            zombie.suffer_damage(self._damage)
        self._hp = 0