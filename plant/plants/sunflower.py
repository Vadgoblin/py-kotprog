from config import Config
import spriteLoader
from plant.plants.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plant.plantManager import PlantManager


config = Config().plant


def _get_sprite():
    sprite_path = config["sunflower"]["sprite"]
    width = config["width"]
    height = config["height"]
    return spriteLoader.load(sprite_path, (width, height))


class Sunflower(AbstractPlant):
    def __init__(self, plant_manager: "PlantManager", row, col):
        hp = config["sunflower"]["hp"]
        super().__init__(plant_manager, row, col, hp)
        self.sun_timeout = config["sunflower"]["sun_spawn_interval"] / 2
        self._sprite = _get_sprite()

    def on_tick(self):
        if self.sun_timeout > 0:
            self.sun_timeout -= 1
            return

        self._plant_manager.spawn_sun(self._row, self._col)
        self.sun_timeout = config["sunflower"]["sun_spawn_interval"]