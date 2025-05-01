from config import Config
import spriteLoader
from plant.abstractPlant import AbstractPlant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from plant.plantManager import PlantManager


config = Config().plant


def _get_sprite():
    sprite_path = config["wallnut"]["sprite"]
    width = config["width"]
    height = config["height"]
    return spriteLoader.load(sprite_path, (width, height))

class Wallnut(AbstractPlant):
    def __init__(self, plant_manager: "PlantManager", row, col):
        hp = config["wallnut"]["hp"]
        super().__init__(plant_manager, row, col, hp)
        self._sprite = _get_sprite()

    def on_tick(self):
        pass