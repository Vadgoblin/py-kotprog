from typing import TYPE_CHECKING

from src.pvz.assets.asset_loader import load_sprite
from src.pvz.config.config import Config
from src.pvz.game import sound_player
from src.pvz.game.plant.plants.abstract_plant import AbstractPlant

if TYPE_CHECKING:
    from src.pvz.game.plant.plant_manager import PlantManager

config = Config().plant


def _get_sprite():
    sprite_path = config["cherrybomb"]["sprite"]
    width = config["width"]
    height = config["height"]
    return load_sprite(sprite_path, (width, height))


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
        else:
            self._explode()

    def _explode(self):
        sound_player.play_cherry_bomb()
        zombies = self._plant_manager._game.zombie_manager.get_nearby_zombies(self._row, self._col)
        for zombie in zombies:
            zombie.suffer_damage(self._damage)
        self._hp = 0
